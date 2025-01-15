from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

# Create your models here.

class SalaModel(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    ubicacion = models.CharField(max_length=200)
    equipamiento = models.TextField()
    disponibilidad = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
    
class ReservaModel(models.Model):
    sala = models.ForeignKey(SalaModel, on_delete=models.CASCADE)
    nombre_cliente = models.CharField(max_length=100)
    fecha_reserva = models.DateField()
    hora_inicio = models.TimeField()
    hora_termino = models.TimeField()
    estado = models.CharField(choices=[('Confirmada','Confirmada'), ('Pendiente', 'Pendiente'), ('Cancelada', 'Cancelada')], max_length=50)
    
    def clean(self):
        # Validación de conflicto de horarios
        if self.hora_inicio >= self.hora_termino:
            raise ValidationError("La hora de inicio debe ser anterior a la hora de término.")
        
        # Verificar si ya existe una reserva en el mismo rango de tiempo
        if ReservaModel.objects.filter(
            sala=self.sala,
            fecha_reserva=self.fecha_reserva,
            hora_inicio__lt=self.hora_termino,
            hora_termino__gt=self.hora_inicio
        ).exists():
            raise ValidationError("Ya existe una reserva en este horario para la sala.")
    
    def __str__(self):
        return f"{self.sala.nombre} - {self.fecha_reserva}"