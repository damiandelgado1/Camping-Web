from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import MakeReservation
from .models import Reservation
from cabin.models import Cabin


# Create a New Reservation by Client
@login_required
def ReservationCreate(request, id):
    if request.method == "POST":
        form = MakeReservation(request.POST)

        if form.is_valid():
            persons = form.cleaned_data['persons']
            entrance = form.cleaned_data['entrance']
            exit = form.cleaned_data['exit']

            cabin = Cabin.objects.get(pk=id)

            if exit <= entrance:
                messages.error(request, "Las Fechas deben ser Diferentes")
            
            elif persons > cabin.rooms:
                messages.error(request, "El numero de Personas supera el Maximo permitido")
            
            reservation = Reservation(
                client = request.user,
                accommodation = Cabin,
                persons = persons,
                entrance = entrance,
                exit = exit
            )
            
            reservation = get_object_or_404(Reservation, pk=id, client=request.user)
            reservation.save()
            messages.success(request, "Reserva creada Correctamente")
        
        else:
            messages.error(request, "Debe completar el Formulario de Reserva")

# See reserv created by Client
def ReservationDetail(request, id):
    reservation = Reservation.objects.get(pk=id)

    context = {
        "Reserva": reservation
    }

    return render(request, "reserv/ReservationDetail.html", context)

# Modify reserv for update data
def ReservationModify(request, id):
    reservation = get_object_or_404(Reservation, pk=id, client=request.user)
    cabin = reservation.accommodation

    if request.method == "POST":
        form = MakeReservation(request.POST, instance=reservation)

        if form.is_valid():
            persons = form.cleaned_data['persons']
            entrance = form.cleaned_data['entrance']
            exit = form.cleaned_data['exit']

            if persons > cabin.rooms:
                messages.error(request, "Nro. de Personas supera el Maximo permitido")

            elif exit < entrance:
                messages.error(request, "Las Fechas deben ser Diferentes")

            else:
                reservation.save()
                messages.info(request, "Nro. de Personas modificado")
                messages.success(request, "Reserva modificada Correctamente")

        else:
            messages.error(request, "Formulario Invalido. Revisa los Datos")
    else:
        form = MakeReservation(instance=reservation)

    return render(request, "reserv/ReservationModify.html", {'form': form, 'reservation': reservation})

# Cancel reservation
def ReservationCancel(request, id):
    reservation = get_object_or_404(Reservation, pk=id, client=request.user)

    if request.method == "POST":

        reservation.delete()
        messages.info(request, "Reserva cancelada")
        return redirect(reverse("main/home.html"))