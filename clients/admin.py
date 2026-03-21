from django.contrib import admin
from .models import User

# Clients register
@admin.register(User)
class UsertAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone")
    search_fields = ("first_name", "email", "phone")