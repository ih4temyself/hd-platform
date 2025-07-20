from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from ckeditor.fields import RichTextField

class Section(models.Model):
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(unique=True)
    authors = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name="sections"
    )

    def __str__(self):
        return self.name
    
class Article(models.Model):
    DRAFT, PUBLISHED = "draft", "pub"
    STATUS_CHOICES = [(DRAFT, "Draft"), (PUBLISHED, "Published")]

    section = models.ForeignKey(Section, on_delete=models.PROTECT, related_name="articles")
    authors = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="articles")
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    hero_image = models.ImageField(upload_to="articles/hero/", blank=True, null=True)
    body = RichTextField()
    status = models.CharField(max_length=5, choices=STATUS_CHOICES, default=DRAFT)
    published_at = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:50]
        if self.status == self.PUBLISHED and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ("-published_at",)

    def __str__(self):
        return self.title