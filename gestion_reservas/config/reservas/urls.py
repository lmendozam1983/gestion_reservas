from django.urls import path 
from . import views 

urlpatterns = [
    path('salas/', views.lista_salas, name='lista_salas'),
    path('salas/<int:pk>',views.detalle_sala, name='detalle_sala'), 
    path('salas/agregar_salas', views.agregar_salas, name='agregar_salas'), 
    path('salas/<int:pk>/editar/', views.editar_sala, name='editar_sala'),
    path('salas/<int:pk>/eliminar/', views.eliminar_sala, name='eliminar_sala'),
    path('reservas/', views.lista_reservas, name='reservas'),
    path('reservas/agregar_reserva', views.agregar_reserva, name='agregar_reserva'),
    path('reservas/<int:pk>', views.editar_reserva, name='editar_reserva'),
    path('reservas/<int:reserva_pk>/eliminar', views.eliminar_reserva, name='eliminar_reserva'),
]