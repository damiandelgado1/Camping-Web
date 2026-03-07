from django.contrib import admin
from .models import Reservation

# View actual Reservs
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("name", "last_name", "email", "entrance", "exit")
    search_fields = ("name", "entrance", "exit")