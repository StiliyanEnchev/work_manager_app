from . import views
from django.urls import path

from jobs.views import CreateJobView, JobListView, EditJobView, DeleteJobView, JobDetailsView, ApplyForJobView

urlpatterns = [
    path('create-job/', CreateJobView.as_view(), name='create-job'),
    path('dashboard/', JobListView.as_view(), name='dashboard'),
    path('edit-job/<int:pk>/', EditJobView.as_view(), name='edit-job'),
    path('delete-job/<int:pk>/', DeleteJobView.as_view(), name='delete-job'),
    path('job-details/<int:pk>/', JobDetailsView.as_view(), name='job-details'),
    path('application/<int:pk>/', ApplyForJobView.as_view(), name='apply-for-job'),
    path('sent/', views.successfull, name='successfull'),
    path('unsuccessfull/', views.unsuccessfull, name='unsuccessfull'),
    path('my-jobs/', views.candidates_dashboard, name='my-jobs')

]
