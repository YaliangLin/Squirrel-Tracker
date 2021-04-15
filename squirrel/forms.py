from django.forms import ModelForm
from .models import biaoge

class SquirrelForm(ModelForm):
    class Meta:
        model = biaoge
        fields = '__all__'