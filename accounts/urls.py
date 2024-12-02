from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views import UserRegistrationView, ProfileDetailView, ProfileUpdateView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('details/<int:pk>/', ProfileDetailView.as_view(), name='details'),
    path('edit/<int:pk>/', ProfileUpdateView.as_view(), name='edit-profile'),

]