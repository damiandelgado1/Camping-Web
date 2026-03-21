from django.contrib import admin
from django.urls import path
from reservation.views import ReservationCreate, ReservationDetail, ReservationModify, ReservationCancel

app_name = "reservation"

urlpatterns = [
    path('create/<int:id>/', ReservationCreate, name="reserva_create"),
    path('detail/<int:id>/', ReservationDetail, name="reserva_detail"),
    path('modify/<int:id>/', ReservationModify, name="reserva_modify"),
    path('cancel/<int:id>/', ReservationCancel, name="reserva_cancel"),
]