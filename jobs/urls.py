from django.urls import path

from jobs.views import CreateJobView, JobListView, EditJobView, DeleteJobView, JobDetailsView

urlpatterns = [
    path('create/', CreateJobView.as_view(), name='create-job'),
    path('dashboard/', JobListView.as_view(), name='dashboard'),
    path('edit/<int:pk>/', EditJobView.as_view(), name='edit-job'),
    path('delete/<int:pk>/', DeleteJobView.as_view(), name='delete-job'),
    path('details/<int:pk>/', JobDetailsView.as_view(), name='job-details'),
]