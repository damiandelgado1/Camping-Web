from django.db import models
from django.utils import timezone
from clients.models import User
from cabin.models import Cabin

# Data of the Reservation
class Reservation(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    persons = models.IntegerField()
    accommodation = models.ForeignKey(Cabin, on_delete=models.CASCADE)
    entrance = models.DateTimeField(verbose_name="Fecha y Hora de Entrada" ,default=timezone.now)
    exit = models.DateTimeField(verbose_name="Fecha y Hora de Salida")

    def __str__(self):
        return f"Reserva hecha por {self.client}, Cabaña reservada: {self.accommodation}, Fecha de Entrada {self.entrance} y Fecha de Salida {self.exit}"