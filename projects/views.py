from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Project
from django.template import loader
from django.http import Http404

# Create your views here.
def index(request):
    projects = Project.objects.all()
    context={
        "projects": projects,
    }
    return render(request, "projects/index.html", context)

def detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'projects/detail.html', {"project": project})