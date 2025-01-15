from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

class SalaModel(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    ubicacion = models.CharField(max_length=200)
    equipamiento = models.TextField()
    
    def __str__(self):
        return self.nombre
    @property
    def disponibilidad(self):
        # Calcula si hay reservas activas en esta sala
        reservas_activas = self.reservas.filter(
            hora_termino__gte=timezone.now().time(),
            fecha_reserva__gte=timezone.now().date()
        )
        return not reservas_activas.exists()
    
    @property
    def disponibilidad_texto(self):
        return "Disponible" if self.disponibilidad else "No disponible"
        
class ReservaModel(models.Model):
    sala = models.ForeignKey(SalaModel, on_delete=models.CASCADE, related_name="reservas")  # Agregado related_name
    nombre_cliente = models.CharField(max_length=100)
    fecha_reserva = models.DateField()
    hora_inicio = models.TimeField()
    hora_termino = models.TimeField()
    estado = models.CharField(
        choices=[('Confirmada', 'Confirmada'), ('Pendiente', 'Pendiente'), ('Cancelada', 'Cancelada')],
        max_length=50
    )
    
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
        return f"Reserva de {self.nombre_cliente} en {self.sala.nombre}"
