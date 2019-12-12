from django.urls import path

from . import views

urlpatterns = [
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/add/', views.add_tasks, name='add_task'),
    path('tasks/<int:task_id>/edit/', views.edit_tasks, name='edit_task'),
]
