from django.forms import ModelForm
from .models import Todowoo

class TodoForm(ModelForm):
    class Meta:
        model = Todowoo
        fields = ['title', 'memo', 'important']
