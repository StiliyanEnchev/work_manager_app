# Generated by Django 5.1.3 on 2024-12-10 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_customuser_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'permissions': [('view_user', 'Can view user'), ('change_user', 'Can change user'), ('delete_user', 'Can delete user')]},
        ),
    ]