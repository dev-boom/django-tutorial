from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Task
from .forms import TaskForm

import datetime


def tasks(request):
    tasks = Task.objects.filter(user=request.user).order_by('-date')
    context = {'tasks': tasks}
    return render(request, 'atato_to_do/tasks.html', context)


def add_tasks(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TaskForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            Task.objects.create(user=user, name=name, date=datetime.datetime.now())
            return HttpResponseRedirect('/tasks/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = TaskForm()
    return render(request, 'atato_to_do/add_task.html', {'form': form})


def edit_tasks(request, task_id):
    return HttpResponse("You're looking at task %s" % task_id)
