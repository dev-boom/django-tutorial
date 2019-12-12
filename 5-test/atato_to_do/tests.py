from django.contrib.auth.models import User
from django.test import TestCase

from .models import Task


class TaskModelTests(TestCase):
    # fixtures = ['fixtures.json'] <-- you can add fixtures data too

    def setUp(self):
        self.user_1 = User.objects.create_user(
            username='user_1', email='user1@atato.com', password='password')
        self.user_2 = User.objects.create_user(
            username='user_2', email='user2@atato.com', password='password')

    def test_get_tasks_when_there_no_task_created(self):
        query_1 = Task.objects.get_tasks(user=self.user_1).exists()
        self.assertFalse(query_1)

    def test_get_tasks_task_created(self):
        Task.objects.create(user=self.user_1, name='Task 1')
        query_1 = Task.objects.get_tasks(user=self.user_1).all()
        self.assertEqual(len(query_1), 1)

        Task.objects.create(user=self.user_1, name='Task 2')
        query_2 = Task.objects.get_tasks(user=self.user_1).all()
        self.assertEqual(len(query_2), 2)

    def test_get_tasks_task_created_with_different_user(self):
        Task.objects.create(user=self.user_1, name='Task 1')
        query_1 = Task.objects.get_tasks(user=self.user_1).all()
        self.assertEqual(len(query_1), 1)
        self.assertEqual(query_1.first().name, 'Task 1')

        Task.objects.create(user=self.user_2, name='Task 2')
        query_2 = Task.objects.get_tasks(user=self.user_2).all()
        self.assertEqual(len(query_2), 1)
        self.assertEqual(query_2.first().name, 'Task 2')
