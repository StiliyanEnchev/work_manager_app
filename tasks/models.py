from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


# Create your models here.
class Task(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(4, message='Name must be at least 3 characters')
        ],
        unique=True
    )

    description = models.TextField(validators=[
        MinLengthValidator(25, message='Description must be at least 25 characters')
    ])

    done = models.BooleanField(default=False)

    reward = models.IntegerField(
        validators=[MinValueValidator(1, message='Reward must be at least 1$'), ]
    )
    account = models.ForeignKey(
        to='accounts.CustomUser',
        on_delete=models.CASCADE,
        related_name='tasks'
    )

    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
