from django.contrib import admin
from .models import Reservation

# View actual Reservs
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("client", "cabin", "entrance", "exit")
    search_fields = ("client", "cabin")