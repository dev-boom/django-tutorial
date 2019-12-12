### Create New App

```sh
python manage.py startapp atato_to_do

```

New Folder Created
```
atato_to_do/
  __init__.py
  admin.py
  apps.py
  migrations/
      __init__.py
  models.py
  tests.py
  views.py
```

### Create Model
in a `atato_to_do > models.py`

add `Task` Model

``` python
from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    is_done = models.BooleanField(default=False)
```

For More Info [https://docs.djangoproject.com/en/2.1/ref/models/fields/](https://docs.djangoproject.com/en/2.1/ref/models/fields/)

add `atato_django_demo` in `setting.py`

``` python
INSTALLED_APPS = [
    'atato_to_do.apps.AtatoToDoConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

### Migrate
``` sh
$ python manage.py makemigrations atato_to_do
```

You will see migration new files generated in `atato_to_do > migrations` start with 001 and ends with date time.

Run migration with
``` sh
$ python manage.py migrate
```

### Creating an admin user
``` sh
python manage.py createsuperuser
```

``` sh
Username: admin
```

``` sh
Email address: admin@atato.com
```

``` sh
Password: **********
Password (again): *********
```

you can go to admin in `http://localhost:8000/admin/`

### Display Task in To Do

in `atato_to_do > admin.py`

``` python
from .models import Task

admin.site.register(Task)
```
