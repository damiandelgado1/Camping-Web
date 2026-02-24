from django.db import models
from django.utils import timezone

# Data of the Reservation
class Reservation(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre del Cliente")
    last_name = models.CharField(max_length=100, verbose_name="Apellido del Cliente")
    email = models.CharField(max_length=50, verbose_name="Email del Cliente")
    persons = models.IntegerField()
    entrance = models.DateTimeField(verbose_name="Fecha y Hora de Entrada" ,default=timezone.now)
    exit = models.DateTimeField(verbose_name="Fecha y Hora de Salida")

    def __str__(self):
        return self.name, self.email, self.persons, self.entrance, self.exit