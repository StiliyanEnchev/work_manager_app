from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


# Create your models here.
class Job(models.Model):
    title = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(4, message='Name must be at least 3 characters')
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
        related_name='jobs'
    )

    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
