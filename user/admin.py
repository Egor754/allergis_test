from django.contrib import admin
from django.contrib.admin import ModelAdmin

from user.models import User


@admin.register(User)
class UserAdmin(ModelAdmin):
    """UI for User model."""
    ordering = ("email", )
    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_superuser",
    )
    search_fields = (
        "first_name",
        "last_name",
        "email",
    )

