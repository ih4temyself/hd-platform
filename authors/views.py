# authors/views.py
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import redirect
from articles.models import Article
from .forms import ArticleForm
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
        obj.status = Article.DRAFT
        obj.save()
        obj.authors.add(self.request.user)
        messages.success(self.request, "Draft saved!")
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
