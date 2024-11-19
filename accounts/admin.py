from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import CustomUser


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password1', 'password2', 'bio', 'type', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )