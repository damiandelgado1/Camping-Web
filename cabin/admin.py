from django.contrib import admin
from .models import Cabin

# View Cabins availabilitys
@admin.register(Cabin)
class CabinAdmin(admin.ModelAdmin):
    list_display = ("number", "rooms", "bathrooms", "price", "show_home")
    search_fields = ("number", "show_home")