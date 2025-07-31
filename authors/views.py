from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.shortcuts import redirect
from django.contrib.auth import logout
from articles.models import Article
from .forms import ArticleForm, ProfileForm
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage

@csrf_exempt
def editor_upload(request):
    if request.method == "POST":
        file = request.FILES.get("file")
        if file:
            file_path = default_storage.save(f"uploads/{file.name}", file)
            file_url = default_storage.url(file_path)
            return JsonResponse({"location": file_url})
        return JsonResponse({"error": "No file provided"}, status=400)
    return JsonResponse({"error": "Invalid request"}, status=400)

def logout_get(request):
    logout(request)
    return redirect('authors:login')

class AuthorCheckMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name="Authors").exists()

class Dashboard(LoginRequiredMixin, AuthorCheckMixin, ListView):
    template_name = "authors/dashboard.html"
    paginate_by = 20

    def get_queryset(self):
        return Article.objects.filter(authors=self.request.user)

class ArticleCreate(LoginRequiredMixin, AuthorCheckMixin, CreateView):
    template_name = "authors/article_form.html"
    form_class = ArticleForm
    success_url = reverse_lazy("authors:dashboard")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        obj = form.save(commit=False)
        if not obj.status:
            obj.status = Article.DRAFT
        obj.save()
        obj.authors.add(self.request.user)
        
        if obj.status == Article.PUBLISHED:
            messages.success(self.request, "Article published successfully!")
        else:
            messages.success(self.request, "Draft saved successfully!")
        return super().form_valid(form)

class ArticleUpdate(LoginRequiredMixin, AuthorCheckMixin, UpdateView):
    model = Article
    template_name = "authors/article_form.html"
    form_class = ArticleForm
    success_url = reverse_lazy("authors:dashboard")

    def get_queryset(self):
        return Article.objects.filter(authors=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        obj = form.save(commit=False)
        if obj.status == Article.PUBLISHED and not obj.published_at:
            from django.utils import timezone
            obj.published_at = timezone.now()
        obj.save()
        
        if obj.status == Article.PUBLISHED:
            messages.success(self.request, "Article published successfully!")
        else:
            messages.success(self.request, "Draft updated successfully!")
        return super().form_valid(form)

class ArticleDelete(LoginRequiredMixin, AuthorCheckMixin, DeleteView):
    model = Article
    success_url = reverse_lazy("authors:dashboard")
    
    def get_queryset(self):
        return Article.objects.filter(authors=self.request.user)
    
    def delete(self, request, *args, **kwargs):
        article = self.get_object()
        messages.success(request, f"Article '{article.title}' deleted successfully!")
        return super().delete(request, *args, **kwargs)

class AuthorProfile(LoginRequiredMixin, DetailView):
    template_name = "authors/profile.html"
    model = Article
    context_object_name = "author"
    
    def get_object(self):
        return self.request.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['published_articles'] = Article.objects.filter(
            authors=self.request.user, 
            status=Article.PUBLISHED
        ).order_by('-published_at')
        context['draft_articles'] = Article.objects.filter(
            authors=self.request.user, 
            status=Article.DRAFT
        ).order_by('-updated_at')
        # Add sections the user has access to
        context['user_sections'] = self.request.user.sections.all().order_by('name')
        return context

class ProfileEdit(LoginRequiredMixin, UpdateView):
    template_name = "authors/profile_edit.html"
    form_class = ProfileForm
    success_url = reverse_lazy("authors:profile")
    
    def get_object(self):
        return self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, "Profile updated successfully!")
        return super().form_valid(form)
