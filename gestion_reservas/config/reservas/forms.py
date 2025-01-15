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

    def clean(self):
        # Llama al método clean original para obtener datos ya validados
        cleaned_data = super().clean()
        sala = cleaned_data.get('sala')
        hora_inicio = cleaned_data.get('hora_inicio')
        hora_termino = cleaned_data.get('hora_termino')

        # Validar que los campos estén completos
        if not sala or not hora_inicio or not hora_termino:
            return cleaned_data

        # Verificar si hay conflictos de horario
        conflictos = ReservaModel.objects.filter(
            sala=sala,
            hora_inicio__lt=hora_termino,  # Conflicto: comienza antes de que termine esta
            hora_termino__gt=hora_inicio   # Conflicto: termina después de que comience esta
        )

        if conflictos.exists():
            raise ValidationError("Ya existe una reserva en este horario para esta sala.")

        return cleaned_data

