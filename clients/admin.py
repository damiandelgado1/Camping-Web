from django.contrib import admin
from .models import Client

# Clients register
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("first_name", "email", "phone")
    search_fields = ("first_name", "phone")