from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'forms-control',
                'placeholder': 'Введите название'
        }),
            "task": Textarea(attrs={
                'class': 'forms-control',
                'placeholder': 'Введите описание'
         })
        }









