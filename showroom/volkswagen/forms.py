from .models import clients1
from django.forms import ModelForm, TextInput, NumberInput
class сlients1Form(ModelForm):
    class Meta:
        model = clients1
        fields=['name', 'num', 'model']

        widgets = {
            'name': TextInput(attrs={
                'class': 'NAME',
                'placeholder': 'Имя'
            }),
            'num': NumberInput(attrs={
                'class': 'NUMBER',
                'placeholder': 'Номер телефона в формате 7XXXXXXXXXX'
            }),
            'model': TextInput(attrs={
                'class': 'MODEL',
                'placeholder': 'Модель'
            })
        }
