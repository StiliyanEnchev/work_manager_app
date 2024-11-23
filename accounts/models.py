from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    class TypeChoices(models.TextChoices):
        JobPoster = 'Job Poster', 'Job Poster'
        Freelancer = 'Freelancer', 'Freelancer'

    bio = models.TextField(blank=True)
    type = models.CharField(choices=TypeChoices)
    email = models.EmailField(unique=True)
