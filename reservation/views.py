from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Reservation
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from reservation.decorators import client_can_modify_or_delete_reservation

# Show detail of the Reservation
class ReservationDetail(DetailView):
    model = Reservation
    template_name = "reserv/ReservationDetail.html"
    context_object_name = 'Reserva'

# Create new Reservation for a Cabin
@method_decorator(login_required, name='dispatch')
class ReservationMake(CreateView):
    model = Reservation
    template_name = "reserv/ReservationMake.html"
    fields = ["number", "description", "rooms", "bathroom", "dining", "kitchen", "availability", "price", "show_home"]
    success_url = reverse_lazy('reserv:CabinList')

# Modify a Reservation exists
@method_decorator(client_can_modify_or_delete_reservation, name='dispatch')
class ReservationModify(UpdateView):
    model = Reservation
    template_name = "reserv/ReservationModify.html"
    fields = ["description", "rooms", "availability"]
    success_url = reverse_lazy('reserv:CabinList')

# Cancel Reservation
@method_decorator(client_can_modify_or_delete_reservation, name='dispatch')
class ReservationCancel(DeleteView):
    model = Reservation
    template_name = "reserv/ReservationCancel.html"