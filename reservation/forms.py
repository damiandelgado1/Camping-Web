from django.utils import timezone
from django import forms
from django.core.exceptions import ValidationError

# Make new Reservation
class MakeReservation(forms.Form):
    persons = forms.IntegerField()
    entrance = forms.DateTimeField()
    exit = forms.DateTimeField()

    def clean_entrance_exit(self):
        entrance = self.cleaned_data.get("entrance")
        exit = self.cleaned_data.get("exit")

        if entrance == exit:
            raise ValidationError("No puedes reservar la Cabaña solo por el Dia")
        elif exit < entrance:
            raise ValidationError("No es valido Salir antes de la Entrada")