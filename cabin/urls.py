from django.contrib import admin
from django.urls import path
from cabin.views import cabins_list, cabin_detail

app_name = "cabin"

urlpatterns = [
    path('', cabins_list, name="cabins"),
    path('<int:id>/', cabin_detail, name="cabin"),
]