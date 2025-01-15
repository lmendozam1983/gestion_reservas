from django.apps import AppConfig


class ReservasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reservas'
    verbose_name = 'Reservas'
    
    def ready(self):
        import reservas.signals  # Importa el archivo de señales