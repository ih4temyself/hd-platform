from django.core.management.base import BaseCommand
from articles.models import Article
from django.utils import timezone
from django.utils.text import slugify


class Command(BaseCommand):
    help = 'Fix articles with empty or invalid slugs'

    def handle(self, *args, **options):
        articles_without_slugs = Article.objects.filter(slug='')
        self.stdout.write(f"Found {articles_without_slugs.count()} articles with empty slugs")
        
        fixed_count = 0
        for article in articles_without_slugs:
            # Generate slug from title, fallback to timestamp if title is empty
            if article.title and article.title.strip():
                base_slug = slugify(article.title)
                if not base_slug:  # If slugify returns empty string
                    base_slug = f"article-{timezone.now().strftime('%Y%m%d-%H%M%S')}"
            else:
                base_slug = f"article-{timezone.now().strftime('%Y%m%d-%H%M%S')}"
            
            # Ensure slug is not too long and is unique
            new_slug = base_slug[:50]
            
            # If slug already exists, append a number
            counter = 1
            original_slug = new_slug
            while Article.objects.filter(slug=new_slug).exclude(pk=article.pk).exists():
                new_slug = f"{original_slug}-{counter}"
                counter += 1
                if len(new_slug) > 50:
                    new_slug = f"{original_slug[:40]}-{counter}"
            
            article.slug = new_slug
            article.save()
            fixed_count += 1
            self.stdout.write(f"Fixed slug for article '{article.title}': {new_slug}")
        
        self.stdout.write(
            self.style.SUCCESS(f"Successfully fixed {fixed_count} article slugs")
        ) 