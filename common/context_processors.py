from django.db.models import Avg
from .models import Feedback


def average_rating_processor(request):
    average_rating = Feedback.objects.aggregate(Avg('rating'))['rating__avg']

    return {
        'average_rating': round(average_rating, 2) if average_rating else None
    }
