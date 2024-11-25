from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from jobs.forms import CreateJobForm, DashBoardPage
from jobs.models import Job


# Create your views here.
class CreateJobView(CreateView):
    model = Job
    template_name = 'job/create.html'
    form_class = CreateJobForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class JobListView(ListView):
    model = Job
    form_class = DashBoardPage
    template_name = 'job/dashboard.html'

    def get_queryset(self):
        return Job.objects.filter(taken=False).order_by('-created_on')