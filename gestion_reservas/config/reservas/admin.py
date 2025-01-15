from django.contrib import admin
from .models import SalaModel, ReservaModel
# Register your models here.
@admin.register(SalaModel)
class SalaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'capacidad', 'ubicacion', 'mostrar_disponibilidad')
    search_fields = ('nombre', 'capacidad', 'ubicacion')
    list_filter = ('capacidad', 'ubicacion')
    ordering = ('nombre', 'id')
    
    @admin.display(boolean=True, description='Disponibilidad')
    def mostrar_disponibilidad(self, obj):
        return obj.disponibilidad

    def filtro_disponibilidad(self, request, queryset):
        filtro = request.GET.get('filtro_disponibilidad')
        if filtro == 'disponible':
            return queryset.filter(reservas__isnull=True)
        elif filtro == 'ocupado':
            return queryset.filter(reservas__isnull=False)
        return queryset


@admin.register(ReservaModel)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('sala', 'nombre_cliente', 'fecha_reserva', 'hora_inicio', 'hora_termino', 'estado')
    search_fields = ('sala', 'nombre_cliente','estado')
    list_filter = ('sala', 'nombre_cliente', 'estado')
    ordering = ('sala', 'id')
    
