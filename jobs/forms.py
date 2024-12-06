from django import forms

from common.mixins import FormDisableMixin
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


class EditJobForm(CreateJobForm):
    pass

class DeleteJobForm(FormDisableMixin, EditJobForm):
    read_only_fields = ['title', 'description', 'salary_per_month', 'created_on']

