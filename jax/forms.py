from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from jax.models import Task

class TaskAdminForm(forms.ModelForm):
    # content = forms.CharField(widget=CKEditorWidget())
    
    class Meta:
        model = Task
        fields = '__all__'
