# Generated by Django 5.1.3 on 2024-12-10 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_customuser_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='type',
            field=models.CharField(choices=[('Job Poster', 'Job Poster'), ('Freelancer', 'Freelancer')]),
        ),
    ]