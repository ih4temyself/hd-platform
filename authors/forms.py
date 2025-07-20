from django import forms
from articles.models import Article, Section

class ArticleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Extract user from kwargs
        super().__init__(*args, **kwargs)
        if user:
            # Filter sections to those the user is associated with
            self.fields['section'].queryset = Section.objects.filter(authors=user)

    class Meta:
        model = Article
        fields = ['title', 'body', 'section', 'hero_image']