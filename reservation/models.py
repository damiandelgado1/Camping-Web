from django.db import models
from cabin.models import Cabin
from clients.models import Client
from django.utils import timezone

# Data of the Reservation
class Reservation(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    persons = models.IntegerField()
    entrance = models.DateTimeField(verbose_name="Fecha y Hora de Entrada" ,default=timezone.now)
    exit = models.DateTimeField(verbose_name="Fecha y Hora de Salida")
    cabin = models.OneToOneField(Cabin, on_delete=models.CASCADE)

    def __str__(self):
        return self.client, self.persons, self.entrance, self.exist, self.cabin