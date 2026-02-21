from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('clients/', include("clients.urls", namespace="clients")),
    path('cabin/', include("cabin.urls", namespace="cabin")),
    path('reservarion/', include("reservation.urls", namespace="reservation")),
    path('admin/', admin.site.urls),
]