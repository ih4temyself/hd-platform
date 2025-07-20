from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):                       
    bio   = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)


    @property
    def is_author(self):
        return self.groups.filter(name="Authors").exists()
