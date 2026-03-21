from django.contrib import admin
from django.urls import path
from cabin.views import CabinList, CabinDetail, CabinCreate, CabinUpdate, CabinDelete

app_name = "cabin"

urlpatterns = [
    path('', CabinList.as_view(), name="cabaña_list"),
    path('create/', CabinCreate.as_view(), name="cabaña_create"),
    path('detail/<int:id>/', CabinDetail.as_view(), name="cabaña_detail"),
    path('update/<int:id>/', CabinUpdate.as_view(), name="cabaña_update"),
    path('delete/<int:id>/', CabinDelete.as_view(), name="cabaña_delete"),
]