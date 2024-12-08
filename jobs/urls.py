from . import views
from django.urls import path

from jobs.views import CreateJobView, JobListView, EditJobView, DeleteJobView, JobDetailsView, ApplyForJobView

urlpatterns = [
    path('create/', CreateJobView.as_view(), name='create-job'),
    path('dashboard/', JobListView.as_view(), name='dashboard'),
    path('edit/<int:pk>/', EditJobView.as_view(), name='edit-job'),
    path('delete/<int:pk>/', DeleteJobView.as_view(), name='delete-job'),
    path('details/<int:pk>/', JobDetailsView.as_view(), name='job-details'),
    path('apply/<int:pk>/', ApplyForJobView.as_view(), name='apply-for-job'),
    path('successfull/', views.successfull, name='successfull'),
    path('unsuccessfull/', views.unsuccessfull, name='unsuccessfull'),
    path('candidates/', views.candidates_dashboard, name='candidates')

]