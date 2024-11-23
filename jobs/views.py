from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from jobs.forms import CreateJobForm
from jobs.models import Job


# Create your views here.
class CreateTaskView(CreateView):
    model = Job
    template_name = 'job/create.html'
    form_class = CreateJobForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)