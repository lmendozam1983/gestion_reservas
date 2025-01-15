from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import ReservaModel

@receiver(post_save, sender=ReservaModel)
def actualizar_disponibilidad_post_save(sender, instance, **kwargs):
    instance.sala.disponibilidad

@receiver(post_delete, sender=ReservaModel)
def actualizar_disponibilidad_post_delete(sender, instance, **kwargs):
    instance.sala.disponibilidad
