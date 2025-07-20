# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(DjangoUserAdmin):

    fieldsets = DjangoUserAdmin.fieldsets + (
        ("Profile", {"fields": ("bio", "avatar")}),
    )
    add_fieldsets = DjangoUserAdmin.add_fieldsets + (
        ("Profile", {"fields": ("bio", "avatar")}),
    )

    list_display = ("username", "email", "is_active", "is_staff")
    search_fields = ("username", "email")
