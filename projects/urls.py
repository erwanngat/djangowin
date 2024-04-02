from django.urls import path

from . import views

app_name = "projects"
urlpatterns = [
    path('', views.home, name="home"),
    path('projects', views.index, name="index"),
    path('project/<int:project_id>', views.detail, name="detail"),
    path('create-project', views.create_project, name="create_project"),
    path('create-task', views.create_project, name="create_task"),
    path('features', views.features, name='features'),
    path('pricing', views.pricing, name='pricing'),
    path('is_finished/<int:project_id>', views.is_finished, name='is_finished'),
    path('task_is_finished/<int:project_id>/<int:task_id>', views.task_is_finished, name='task_is_finished'),
    path('task_is_finished_a/<int:task_id>', views.task_is_finished_a, name='task_is_finished_a'),
    path('delete_task/<int:project_id>/<int:task_id>', views.delete_task, name='delete_task'),
    path('delete_task_a/<int:task_id>', views.delete_task_a, name='delete_task_a'),
    path('delete_project/<int:project_id>', views.delete_project, name='delete_project'),
    path('all_tasks', views.all_tasks, name='all_tasks'),
]