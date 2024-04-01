from django import forms
import datetime

class CreateProjectForm(forms.Form):
    project_name = forms.CharField(label="Project name", max_length=100)
    project_description = forms.CharField(label="Project description", max_length=1000)


class CreateTaskForm(forms.Form):
    task_name = forms.CharField(label="Task name", max_length=100)
    task_description = forms.CharField(label="Task description", max_length=1000)
    task_end_date = forms.DateTimeField(label="end date", initial=datetime.datetime.today)
