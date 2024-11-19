from django.contrib.auth.views import LoginView
from django.urls import path

from accounts.views import UserRegistrationView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login')
]