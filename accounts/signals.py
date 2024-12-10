# my_app/signals.py

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_migrate
from django.dispatch import receiver

from accounts.models import CustomUser
from jobs.models import Job


@receiver(post_migrate)
def create_groups_and_permissions(sender, **kwargs):
    editors_group, created = Group.objects.get_or_create(name="Editors")

    content_type = ContentType.objects.get_for_model(Job)
    add_permission = Permission.objects.get(codename='add_job', content_type=content_type)
    change_permission = Permission.objects.get(codename='change_job', content_type=content_type)
    delete_permission = Permission.objects.get(codename='delete_job', content_type=content_type)
    view_permission = Permission.objects.get(codename='view_job', content_type=content_type)
    editors_group.permissions.add(add_permission, change_permission, delete_permission, view_permission)

    user_managers_group, created = Group.objects.get_or_create(name="User Managers")

    user_content_type = ContentType.objects.get_for_model(CustomUser)
    view_user_permission = Permission.objects.get(codename='view_customuser', content_type=user_content_type)
    change_user_permission = Permission.objects.get(codename='change_customuser', content_type=user_content_type)
    delete_user_permission = Permission.objects.get(codename='delete_customuser', content_type=user_content_type)
    user_managers_group.permissions.add(view_user_permission, change_user_permission, delete_user_permission)
