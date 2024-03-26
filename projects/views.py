from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Project, Users
from django.template import loader
from django.http import Http404
from .forms import CreateProjectForm
from django.utils import timezone
import datetime


# Create your views here.
def home(request):
    return render(request, 'projects/home.html', {})

def index(request):
    projects = Project.objects.all()
    context={
        "projects": projects,
    }
    return render(request, "projects/index.html", context)

def detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'projects/detail.html', {"project": project})

def create_project(request):
    if request.method == 'POST':
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            project_name = form.cleaned_data['project_name']
            project_description = form.cleaned_data['project_description']
            now = datetime.datetime.now()
            project = Project.objects.create(name=project_name, creation_date=now, end_date=None, description=project_description)
            Users.objects.create(project_id=project.pk, user_id=request.user.id)
            return  HttpResponseRedirect("/projects")
    else:
        form = CreateProjectForm()
    return render(request, 'projects/create_project.html', {"form" : form})