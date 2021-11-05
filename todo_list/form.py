from django import forms 
from todo_list.models import Tasklist

 
class TaskForm(forms.ModelForm):
    class Meta:
        model=Tasklist
        fields=['task','done']