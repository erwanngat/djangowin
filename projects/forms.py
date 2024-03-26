from django import forms

class CreateProjectForm(forms.Form):
    project_name = forms.CharField(label="Project name", max_length=100)
    project_description = forms.CharField(label="Project description", max_length=1000)
