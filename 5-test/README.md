### Test

Test Query Tasks correctly

Separate query into `Manager` files for easy unit test

create new file `atato_to_do > managers.py`

``` python
class TaskManager(models.Manager):
    def get_tasks(self, user):
        return super().get_queryset().filter(user=user).order_by('-date')
```

change `atato_to_do > models.py`

``` python
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    is_done = models.BooleanField(default=False)

    objects = TaskManager()
```

change `atato_to_do > views.py`

``` python
def tasks(request):
    tasks = Task.objects.get_tasks(request.user)
    context = {'tasks': tasks}
    return render(request, 'atato_to_do/tasks.html', context)
```

Go to `atato_to_do > test.py`

Please make sure test methods begins with *`test_`*

```python
from .models import Task

class TaskModelTests(TestCase):

    def test_get_tasks(self):
        query_1 = Task.objects.get_tasks(user=None).exists()
        self.assertFalse(query_1)
```

RUN test
inside VM
```sh
$ python manage.py test atato_to_do
```

You can also call specific test case by
```sh
$ atato_to_do.tests.TaskModelTests.test_get_tasks
```

You can also have fixtures where `fixtures.json` is the file you have
``` sh
fixtures = ['fixtures.json']
```

Look at more test cases on `test.py`
