from django.contrib import admin
from .models import Cabin

# View Cabins availabilitys
@admin.register(Cabin)
class CabinAdmin(admin.ModelAdmin):
    list_display = ("number", "rooms", "bathrooms", "availability", "price", "show_home")
    search_fields = ("number", "availability", "show_home")