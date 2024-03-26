from django.urls import path

from . import views

app_name = "projects"
urlpatterns = [
    path('', views.home, name="home"),
    path('projects', views.index, name="index"),
    path('/project/<int:project_id>', views.detail, name="detail"),
    path('create-project', views.create_project, name="create_project"),
    path('create-task', views.create_project, name="create_task"),
]