from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from views import editor_upload

urlpatterns = [
    path("editor-upload/", editor_upload, name="editor_upload"),
]