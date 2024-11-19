from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    class TypeChoices(models.TextChoices):
        LOOKER = 'Looker', 'Looker'
        SEARCHER = 'Searcher', 'Searcher'

    bio = models.TextField(blank=True)
    type = models.CharField(choices=TypeChoices)
