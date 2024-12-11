from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse
from django.views.generic import ListView, CreateView
from .models import Feedback, News
from .forms import FeedbackForm, NewsForm

# Create your views here.
def home(request):
    return render(request, 'common/home.html')


def about(request):
    return render(request, 'common/about.html')


class SubmitFeedbackView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback/submit-feedback.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')


class AddNewsView(CreateView):
    model = News
    form_class = NewsForm
    template_name = 'news/add-news.html'

    def form_valid(self, form):
        messages.success(self.request, 'News item added successfully.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('news')


class NewsListView(ListView):
    model = News
    template_name = 'news/news-list.html'
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.filter(is_active=True).order_by('-published_on')


