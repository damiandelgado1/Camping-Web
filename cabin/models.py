from django.db import models

# Data and Specifications of the Booking
class Cabin(models.Model):
    number = models.IntegerField(verbose_name="Nro. de Cabaña")
    description = models.TextField(verbose_name="Descripcion")
    rooms = models.IntegerField(verbose_name="Nro. de Habitaciones")
    bathrooms = models.IntegerField(verbose_name="Baños")
    dining = models.BooleanField(default=True, verbose_name="Comedor")
    kitchen = models.BooleanField(default=True, verbose_name="Cocina")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    show_home = models.BooleanField("Mostrar en el Inicio", default=False)

    class Meta:
        verbose_name = 'Cabaña'
        verbose_name_plural = 'Cabañas'

    def __str__(self):
        return f"Nro. de Cabaña {self.number}, Precio {self.price}"