from django.urls import path

from common import views
from common.views import NewsListView, SubmitFeedbackView, AddNewsView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('news/', NewsListView.as_view(), name='news'),
    path('add-news/', AddNewsView.as_view(), name='add-news'),
    path('submit-feedback/', SubmitFeedbackView.as_view(), name='submit-feedback'),

]

