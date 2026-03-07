from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cabin

# Show all Cabin
class CabinList(ListView):
    model = Cabin
    template_name = "cabin/CabinList.html"
    context_object_name = 'Cabaña'

# Show detail of the Cabin
class CabinDetail(DetailView):
    model = Cabin
    template_name = "cabin/CabinDetail.html"
    context_object_name = 'Cabaña'

# Create new Cabin for reserv
class CabinCreate(CreateView):
    model = Cabin
    template_name = "cabin/CabinCreate.html"
    fields = ["number", "description", "rooms", "bathroom", "dining", "kitchen", "availability", "price", "show_home"]
    success_url = reverse_lazy('cabin:CabinList')

# Update data Cabin
class CabinUpdate(UpdateView):
    model = Cabin
    template_name = "cabin/CabinUpdate.html"
    fields = ["description", "rooms", "availability"]
    success_url = reverse_lazy('cabin:CabinList')

# Delete a Cabin
class CabinDelete(DeleteView):
    model = Cabin
    template_name = "cabin/CabinDelete.html"