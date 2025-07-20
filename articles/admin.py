from django.contrib import admin
from .models import Section, Article

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    filter_horizontal   = ("authors",)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display    = ("title", "section", "status", "published_at")
    list_filter     = ("section", "status")
    search_fields   = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal   = ("authors",)
