# Generated by Django 5.1.3 on 2024-12-11 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_customuser_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]
