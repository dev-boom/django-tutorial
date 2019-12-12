from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    is_done = models.BooleanField(default=False)


# one_to_one = models.OneToOneField(MyModel)
# many_to_many = models.ManyToManyField(MyModel)
