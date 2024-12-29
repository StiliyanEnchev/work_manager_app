# Generated by Django 5.1.3 on 2024-12-04 16:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=100, unique=True, validators=[django.core.validators.MinLengthValidator(4, message='The title must be at least 3 characters')]),
        ),
    ]
