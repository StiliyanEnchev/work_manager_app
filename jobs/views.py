from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db import IntegrityError
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from jobs.forms import CreateJobForm, DashBoardPage, EditJobForm, DeleteJobForm
from jobs.models import Job, JobApplication


# Create your views here.
class CreateJobView(CreateView):
    model = Job
    template_name = 'job/create.html'
    form_class = CreateJobForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class JobListView(ListView):
    model = Job
    form_class = DashBoardPage
    template_name = 'job/dashboard.html'

    def get_queryset(self):
        return Job.objects.filter(taken=False).order_by('-created_on')


class EditJobView(PermissionRequiredMixin, UpdateView):
    model = Job
    form_class = EditJobForm
    success_url = reverse_lazy('dashboard')
    template_name = 'job/edit.html'
    permission_required = 'jobs.change_job'

    def has_permission(self):

        job = self.get_object()
        if job.owner == self.request.user:
            return True

        return super().has_permission()


class DeleteJobView(DeleteView):
    model = Job
    template_name = 'job/delete-post.html'
    success_url = reverse_lazy('dashboard')
    form_class = DeleteJobForm

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)

    def get_queryset(self):
        return Job.objects.filter(owner=self.request.user)


class JobDetailsView(DetailView):
    template_name = 'job/job_details.html'
    model = Job

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Job.objects.filter(pk=pk)


class ApplyForJobView(LoginRequiredMixin, View):

    def post(self, request, pk, *args, **kwargs):
        job = get_object_or_404(Job, id=pk)
        user = request.user

        try:
            current_job = JobApplication.objects.create(job=job, freelancer=user)
            current_job.bio = user.bio
            current_job.save()
            return redirect('successfull')

        except IntegrityError:
            return redirect('unsuccessfull')


def successfull(request):
    return render(request, 'job/applied.html')


def unsuccessfull(request):
    return render(request, 'job/unsuccessfull.html')


@login_required()
def candidates_dashboard(request):
    jobs = Job.objects.filter(owner=request.user).prefetch_related('applications__freelancer')

    dashboard_data = []
    for job in jobs:
        applications = job.applications.all()
        dashboard_data.append({
            'job': job,
            'applications': applications,
        })

    return render(request, 'job/my-jobs.html', {
        'dashboard_data': dashboard_data
    })


@login_required
def mark_job_taken(request, pk):
    job = get_object_or_404(Job, id=pk)

    if job.owner != request.user:
        return HttpResponseForbidden("You don't have permission to modify this job.")

    job.taken = True
    job.save()

    return redirect('dashboard')