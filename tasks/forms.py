from django import forms

from tasks.models import Task


class BaseTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

