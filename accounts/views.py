from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView

from accounts.forms import CustomUserCreationForm


# Create your views here.

class UserRegistrationView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'profile/profile_detail.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = 'profile/edit_profile.html'
    fields = ['username', 'email', 'bio']
    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('details', kwargs={'pk': self.object.pk})