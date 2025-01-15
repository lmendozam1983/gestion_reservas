from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse
from .models import SalaModel, ReservaModel
from django.core.exceptions import ValidationError
from django.utils import timezone  # Importa timezone desde django.utils
from datetime import timedelta  # Importa timedelta desde datetime
from django.db import IntegrityError  # Importa IntegrityError desde django.db



class LaboratorioModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.sala = SalaModel.objects.create(
            nombre ='Sala Ciencias', 
            capacidad = 30, 
            ubicacion ='Tercer Piso',
            equipamiento = 'Proyector',
            disponibilidad = True,
        )

    def test_nombre(self):
        sala = SalaModel.objects.get(id=self.sala.id)
        self.assertEqual(sala.nombre, 'Sala Ciencias')

    def test_capacidad(self):
        sala = SalaModel.objects.get(id=self.sala.id)
        self.assertEqual(sala.capacidad, 30)

    def test_ubicacion(self):
        sala = SalaModel.objects.get(id=self.sala.id)
        self.assertEqual(sala.ubicacion, 'Tercer Piso')

    def test_equipamiento(self):
        sala = SalaModel.objects.get(id=self.sala.id)
        self.assertEqual(sala.equipamiento, 'Proyector')

    def test_disponibilidad(self):
        sala = SalaModel.objects.get(id=self.sala.id)
        self.assertEqual(sala.disponibilidad, True)


class SalaUrlTest(TestCase):

    def test_sala_url(self):
        response = self.client.get(reverse('lista_salas'))  
        self.assertEqual(response.status_code, 200)


class ReservaModelTest(TestCase):
    
    def setUp(self):
        # Crear una sala para la prueba
        self.sala = SalaModel.objects.create(
            nombre="Sala 1",
            capacidad=30,
            equipamiento="Proyector, Pizarra"
        )
        
        # Crear una reserva inicial
        self.reserva_inicial = ReservaModel.objects.create(
            sala=self.sala,
            fecha_reserva=timezone.now().date(),  # Asegúrate de asignar una fecha válida
            hora_inicio=timezone.now(),
            hora_termino=timezone.now() + timedelta(hours=1)
        )

    def test_reserva_sin_conflictos(self):
        # Crear una reserva en un horario libre (después de la reserva inicial)
        nueva_reserva = ReservaModel.objects.create(
            sala=self.sala,
            fecha_reserva=timezone.now().date(),  # Asigna también la fecha
            hora_inicio=self.reserva_inicial.hora_termino + timedelta(minutes=30),  # Comienza 30 min después de la reserva inicial
            hora_termino=self.reserva_inicial.hora_termino + timedelta(hours=1, minutes=30)
        )
        
        # Verificar que la nueva reserva se ha creado correctamente
        self.assertEqual(ReservaModel.objects.count(), 2)

    def test_reserva_con_conflicto(self):
    # Intentar crear una reserva con un horario conflictivo
        with self.assertRaises(ValidationError):
            ReservaModel.objects.create(
                sala=self.sala,
                fecha_reserva=self.reserva_inicial.fecha_reserva,
                hora_inicio=self.reserva_inicial.hora_inicio + timedelta(minutes=30),
                hora_termino=self.reserva_inicial.hora_termino - timedelta(minutes=30)
        )