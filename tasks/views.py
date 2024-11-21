from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.models import CustomUser
from tasks.forms import BaseTaskForm
from tasks.models import Task


# Create your views here.
class CreateTaskView(CreateView):
    model = Task
    template_name = 'task/create.html'
    form_class = BaseTaskForm
    success_url = reverse_lazy('home')
