from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import Dashboard, ArticleCreate, ArticleUpdate

app_name = "authors"

urlpatterns = [
    path("login/",  LoginView.as_view(template_name="authors/login.html"),  name="login"),
    path("logout/", LogoutView.as_view(next_page="authors:login"),          name="logout"),

    path("",        Dashboard.as_view(),           name="dashboard"),
    path("new/",    ArticleCreate.as_view(),       name="article_new"),
    path("<slug:slug>/edit/", ArticleUpdate.as_view(), name="article_edit"),
]