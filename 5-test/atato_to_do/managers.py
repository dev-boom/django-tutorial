from django.db import models

class TaskManager(models.Manager):
    def get_tasks(self, user):
        return super().get_queryset().filter(user=user).order_by('-date')
