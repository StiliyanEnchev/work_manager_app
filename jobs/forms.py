from django import forms

from jobs.models import Job


class BaseJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'


class CreateJobForm(BaseJobForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['owner', 'taken']

class DashBoardPage(BaseJobForm):
    pass