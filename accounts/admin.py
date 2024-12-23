from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from accounts.models import CustomUser

UserModel = get_user_model()


# Register your models here.
@admin.register(UserModel)
class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        ('User Details', {
            'fields': (
            'username', 'email', 'password1', 'password2', 'groups', 'type', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )

    fieldsets = (
        ('Personal Info', {
            'fields': ('username', 'email', 'first_name', 'last_name', 'password', 'groups', 'type', 'bio', 'is_active',
                       'is_staff', 'is_superuser'),
        }),
    )

    list_display = (
        'username', 'email', 'is_active', 'is_staff', 'is_superuser', 'type'
    )

    list_filter = ('type', 'is_staff')

    ordering = ('username',)
