from django.urls import path

from jobs.views import CreateTaskView

urlpatterns = [
    path('create/', CreateTaskView.as_view(), name='create-job'),

]