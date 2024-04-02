from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Project, Users, Task
from .forms import CreateProjectForm, CreateTaskForm
import datetime
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'projects/home.html', {})

@login_required
def index(request):
    projects = Project.objects.filter(users__user=request.user) 
    username = request.user.username
    data={
        "projects": projects,
        "username": username,
    }
    return render(request, "projects/index.html", data)

def detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    now = datetime.datetime.now()
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task_name = form.cleaned_data['task_name']
            task_description = form.cleaned_data['task_description']
            task_end_date = form.cleaned_data['task_end_date']
            Task.objects.create(name=task_name, description=task_description, creation_date=datetime.datetime.now(), end_date=task_end_date, project_id=project_id)
    else:
        form = CreateTaskForm()
    return render(request, 'projects/detail.html', {"project": project, "form" : form, "now" : now})

def create_project(request):
    if request.method == 'POST':
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            project_name = form.cleaned_data['project_name']
            project_description = form.cleaned_data['project_description']
            now = datetime.datetime.now()
            project = Project.objects.create(name=project_name, creation_date=now, end_date=None, description=project_description)
            Users.objects.create(project_id=project.pk, user_id=request.user.id)
            return HttpResponseRedirect('/projects')
    else:
        form = CreateProjectForm()
    return render(request, 'projects/create_project.html', {"form" : form})

def features(request):
    return render(request, 'projects/features.html', {})

def pricing(request):
    return render(request, 'projects/pricing.html', {})

def is_finished(request, project_id):
    Project.objects.filter(pk=project_id).update(end_date=datetime.datetime.now(), is_finished=True)
    return redirect('projects:index')

def task_is_finished(request, project_id, task_id):
    Task.objects.filter(pk=task_id).update(end_date=datetime.datetime.now(), is_finished=True)
    return redirect('/project/' + str(project_id))

def task_is_finished_a(request, task_id):
    Task.objects.filter(pk=task_id).update(end_date=datetime.datetime.now(), is_finished=True)
    return redirect('projects:all_tasks')

def delete_task(request, project_id, task_id):
    Task.objects.filter(pk=task_id).delete()
    return redirect('/project/' + str(project_id))

def delete_task_a(request, task_id):
    Task.objects.filter(pk=task_id).delete()
    return redirect('projects:all_tasks')

def delete_project(request, project_id):
    Project.objects.filter(pk=project_id).delete()
    return redirect('projects:index')

def all_tasks(request):
    projects = Project.objects.filter(users__user=request.user) 
    tasks = Task.objects.filter(project__in=projects) 
    return render(request, 'projects/all_tasks.html', {'tasks': tasks})

def project_edit(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        project_name = request.POST.get['project_name']
        project_description = request.POST.get['project_description']
        project_creation_date = request.POST.get['project_cration_date']
        project_end_date = request.POST.get['project_end_date']
        project_is_finished = request.POST.get['project_is_finished']
        Project.objects.update(name=project_name, description=project_description, creation_date=project_creation_date, end_date=project_end_date, is_finished=project_is_finished)
    else:
        return render(request, 'projects/project_edit.html', {'project': project})