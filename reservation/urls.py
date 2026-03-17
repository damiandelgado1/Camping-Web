from django.contrib import admin
from django.urls import path
from reservation.views import ReservationDetail, ReservationMake, ReservationModify, ReservationCancel

app_name = "reservation"

urlpatterns = [
    path('detail/<int:id>', ReservationDetail.as_view(), name="reserva_detail"),
    path('make/<int:id>', ReservationMake.as_view(), name="reserva_make"),
    path('modify/<int:id>', ReservationModify.as_view(), name="reserva_modify"),
    path('cancel/<int:id>', ReservationCancel.as_view(), name="reserva_cancel"),
    path('admin/', admin.site.urls)
]