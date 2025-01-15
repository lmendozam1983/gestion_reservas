from django.contrib import admin
from .models import SalaModel, ReservaModel
# Register your models here.

@admin.register(SalaModel)
class SalaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'capacidad', 'ubicacion', 'equipamiento', 'disponibilidad')
    search_fields = ('nombre', 'capacidad', 'ubicacion', 'equipamiento', 'disponibilidad')
    list_filter = ('nombre', 'disponibilidad')
    ordering = ('nombre', 'id')

@admin.register(ReservaModel)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('sala', 'nombre_cliente', 'fecha_reserva', 'hora_inicio', 'hora_termino', 'estado')
    search_fields = ('sala', 'nombre_cliente','estado')
    list_filter = ('sala', 'nombre_cliente', 'estado')
    ordering = ('sala', 'id')
    
