from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.models import CustomUser
from jobs.forms import BaseJobForm
from jobs.models import Job


# Create your views here.
class CreateTaskView(CreateView):
    model = Job
    template_name = 'job/create.html'
    form_class = BaseJobForm
    success_url = reverse_lazy('home')
