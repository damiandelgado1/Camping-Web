from django.shortcuts import render

# Show Home of the Site Camping
def home_site(request):
    return render(request, "main/home.html")

# Show Cabin availability for Rent
def cabin_availability(request):
    return render(request, "cabin/CabinList.html")

# Section to Make new reservation
def create_reservation(request):
    return render(request, "reserv/ReservationMake.html")

# Information account of the Client
def register_account(request):
    return render(request, "main/register.html")

def login_account(request):
    return render(request, "main/login.html")

# About of the Site Cabin
def about_site(request):
    return render(request, "main/about.html")