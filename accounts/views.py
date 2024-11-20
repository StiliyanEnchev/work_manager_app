from django.contrib.auth import login, get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from accounts.forms import CustomUserCreationForm, CustomUserChangeForm


# Create your views here.

class UserRegistrationView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')


class UserProfileUpdateView(UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('home')
    template_name = 'common/user_update.html'

    def get_object(self, queryset=None):
        return self.request.user

