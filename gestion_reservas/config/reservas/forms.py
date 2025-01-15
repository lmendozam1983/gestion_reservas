from django import forms
from .models import SalaModel, ReservaModel

class SalaForm(forms.ModelForm):
    class Meta:
        model = SalaModel  
        fields = '__all__' 
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'capacidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control'}),
            'equipamiento': forms.TextInput(attrs={'class':'form-control'}),
        }
        
from django import forms
from django.core.exceptions import ValidationError
from .models import ReservaModel

class ReservaForm(forms.ModelForm):
    class Meta:
        model = ReservaModel
        fields = '__all__'
        widgets = {
            'hora_inicio': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time',
            }),
            'hora_termino': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time',
            }),
        }




