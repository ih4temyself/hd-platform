from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import Dashboard, ArticleCreate, ArticleUpdate, ArticleDelete, logout_get, AuthorProfile, ProfileEdit

app_name = "authors"

urlpatterns = [
    path("login/",  LoginView.as_view(template_name="authors/login.html"),  name="login"),
    path("logout/", LogoutView.as_view(next_page="authors:login"),          name="logout"),
    path("logout-get/", logout_get,                                          name="logout_get"),

    path("",        Dashboard.as_view(),           name="dashboard"),
    path("profile/", AuthorProfile.as_view(),      name="profile"),
    path("profile/edit/", ProfileEdit.as_view(),   name="profile_edit"),
    path("new/",    ArticleCreate.as_view(),       name="article_new"),
    path("<slug:slug>/edit/", ArticleUpdate.as_view(), name="article_edit"),
    path("<slug:slug>/delete/", ArticleDelete.as_view(), name="article_delete"),
]