from django.utils import timezone
from django import forms
from cabin.models import Cabin

# Make new Reservation
class MakeReservation(forms.Form):
    first_name = forms.CharField(max_length=100, label="Nombre")
    last_name = forms.CharField(max_length=100, label="Apellido")
    email = forms.CharField(max_length=100, label="Email")
    persons = forms.IntegerField()
    entrance = forms.DateTimeField(verbose_name="Fecha y Hora de Entrada" ,default=timezone.now)
    exit = forms.DateTimeField(verbose_name="Fecha y Hora de Salida")

    def cleaned_email(self):
        email = self.cleaned_data.get("email")

        if "@gmail.com" not in email:
            raise forms.ValidationError("Debe ingresar '@gmail.com' en su Email")
        
        if email != '':
            raise forms.ValidationError("Debe Ingresar el Email")

    class Meta:
        model = Cabin
        fields = [
            'Nombre',
            'Apellido',
            'Email',
            'Nro. de Personas',
            'Fecha de Entrada',
            'Fecha de Salida',
        ]