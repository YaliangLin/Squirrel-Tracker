from django.forms import ModelForm

class SquirrelForm(ModelForm):
    class Meta:
        model = chart
        fields = '__all__'
