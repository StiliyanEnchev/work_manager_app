from django.urls import path

from jobs.views import CreateJobView, JobListView, EditJobView

urlpatterns = [
    path('create/', CreateJobView.as_view(), name='create-job'),
    path('dashoard/', JobListView.as_view(), name='dashboard'),
    path('edit/<int:pk>/', EditJobView.as_view(), name='edit-job'),

]