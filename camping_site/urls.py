from django.contrib import admin
from django.urls import path, include
from .views import home_site

urlpatterns = [
    path('', home_site, name="home"),
    path('clients/', include("clients.urls", namespace="client")),
    path('cabin/', include("cabin.urls", namespace="cabin")),
    path('reservation/', include("reservation.urls", namespace="reservation")),
    path('admin/', admin.site.urls),
]