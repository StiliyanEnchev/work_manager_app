from django.conf import settings
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


# Create your models here.
class Job(models.Model):
    title = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(3, message='The title must be at least 3 characters')
        ],
        unique=True
    )

    description = models.TextField(validators=[
        MinLengthValidator(25, message='Description must be at least 25 characters')
    ])

    taken = models.BooleanField(default=False)

    salary_per_month = models.IntegerField(
        validators=[MinValueValidator(800, message='Salary must be at least 800$'), ]
    )
    owner = models.ForeignKey(
        to='accounts.CustomUser',
        on_delete=models.CASCADE,
        related_name='job'
    )

    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class JobApplication(models.Model):
    job = models.ForeignKey('Job', on_delete=models.CASCADE, related_name='applications')
    freelancer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='applications')
    applied_on = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.freelancer} applied for {self.job}"