### Edit View
edit `atato_to_do > views.py`
``` python
from django.contrib.auth.models import User
from django.http import HttpResponse


def tasks(request):
    return HttpResponse("You're looking at tasks")


def add_tasks(request):
    return HttpResponse("You're looking at add task")


def edit_tasks(request, task_id):
    return HttpResponse("You're looking at task %s" % task_id)
```

edit `atato_django_demo > urls.py`
``` python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('atato_to_do.url')),
    path('admin/', admin.site.urls),
]
```

create file `atato_to_do > urls.py` with following parameters
``` python
from django.urls import path

from . import views

urlpatterns = [
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/add/', views.add_tasks, name='add_task'),
    path('tasks/<int:task_id>/edit/', views.edit_tasks, name='edit_task'),
]
```

More info about urls [https://docs.djangoproject.com/en/2.1/topics/http/urls/](https://docs.djangoproject.com/en/2.1/topics/http/urls/)

Go to `http://localhost:8000/tasks`

Go to `http://localhost:8000/tasks/add`

Go to `http://localhost:8000/tasks/1/edit`
Please not you can change `task_id` : `1` to any number

### Create Template
Create folder named `atato_to_do` in `atato_to_do > templates` (atato_to_do > templates > atato_to_do)

Note
```
Template namespacing

Now we might be able to get away with putting our templates directly in atato_to_do/templates (rather than creating another atato_to_do subdirectory), but it would actually be a bad idea. Django will choose the first template it finds whose name matches, and if you had a template with the same name in a different application, Django would be unable to distinguish between them. We need to be able to point Django at the right one, and the easiest way to ensure this is by namespacing them. That is, by putting those templates inside another directory named for the application itself.
```

Add files `add_task.html`, `edit_task.html`, `tasks.html`

Edit `View`

``` python
from .models import Task


def tasks(request):
    tasks = Task.objects.filter(user=request.user).order_by('-date')
    context = {'tasks': tasks}
    return render(request, 'atato_to_do/tasks.html', context)
```

Edit `Template` `tasks.html`

``` python
{% if tasks %}
    <ul>
    {% for task in tasks %}
        <li>
          <span>
          {% if task.is_done %}
          ☑
          {% else %}
          🗸
          {% endif %}
          </span>
          <a href="{% url 'edit_task' task.id %}">{{ task.name }}</a>
        </li>
    {% endfor %}
    </ul>
{% else %}
    <p>No Tasks are available.</p>
{% endif %}
```

You will see `No Tasks are available.`

Go Ahead add tasks in `http:/localhost:8000/admin`

to save fixtures you can type this command inside VM
``` sh
$ python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 4 > fixtures.json
```

to load fixtures do
``` sh
$ python manage.py loaddata fixtures.json
```

### Create Form
[https://docs.djangoproject.com/en/2.1/topics/forms/#building-a-form-in-django](https://docs.djangoproject.com/en/2.1/topics/forms/#building-a-form-in-django)

create files named `forms.py` in `atato_to_do`
``` python
from django import forms

class TaskForm(forms.Form):
    name = forms.CharField(label='task name', max_length=200)
```

edit View in `atato_to_do > views.py`

``` python
from .forms import TaskForm

def add_tasks(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TaskForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # Assume you Login as Admin
            user = request.user
            name = form.cleaned_data['name']
            Task.objects.create(user=user, name=name, date=datetime.datetime.now())
            return HttpResponseRedirect('/tasks/')
        # if a GET (or any other method) we'll create a blank form
    else:
        form = TaskForm()
    return render(request, 'atato_to_do/add_task.html', {'form': form})
```

Go to `http://localhost:8000/tasks/add/` then add new task
