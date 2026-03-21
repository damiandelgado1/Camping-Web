from django.contrib import admin
from .models import Reservation

# View actual Reservs
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("client", "accommodation", "entrance", "exit")
    search_fields = ("client", "accommodation", "entrance", "exit")