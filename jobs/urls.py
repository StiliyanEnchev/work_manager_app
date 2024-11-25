from django.urls import path

from jobs.views import CreateJobView, JobListView

urlpatterns = [
    path('create/', CreateJobView.as_view(), name='create-job'),
    path('dashoard/', JobListView.as_view(), name='dashboard')

]