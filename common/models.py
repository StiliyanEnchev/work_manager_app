from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


class Feedback(models.Model):
    user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        related_name='feedbacks'
    )

    message = models.TextField()

    rating = models.IntegerField(
        choices=[(i, str(i)) for i in range(1, 6)],
        default=1
    )

    created_on = models.DateTimeField(
        default=timezone.now
    )

    def __str__(self):
        return f"Feedback from {self.user.username} - Rating: {self.rating}"


class News(models.Model):
    title = models.CharField(
        max_length=200
    )
    content = models.TextField()

    published_on = models.DateTimeField(default=timezone.now)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
