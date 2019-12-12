from django import forms

class TaskForm(forms.Form):
    name = forms.CharField(label='task name', max_length=200)
