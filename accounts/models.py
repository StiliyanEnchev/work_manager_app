from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

from accounts.validators import only_numbers


# Create your models here.
class CustomUser(AbstractUser):
    class TypeChoices(models.TextChoices):
        JobPoster = 'Job Poster', 'Job Poster'
        Freelancer = 'Freelancer', 'Freelancer'

    bio = models.TextField(blank=True)
    type = models.CharField(choices=TypeChoices)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(validators=[
        MinLengthValidator(10),
        MaxLengthValidator(13),
        only_numbers,
    ])