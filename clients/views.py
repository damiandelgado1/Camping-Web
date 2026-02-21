from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout

from .forms import RegisterClient, LoginClient
from .models import Client

# Register to the Client
def register_view(request):
    if request.POST:
        form = RegisterClient(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['name']
            last_name = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            client = Client.objects.create_client(username, email, phone, password2)

            if client:
                client.first_name = first_name
                client.last_name = last_name
                client.save()

            context = {
                'msg': 'Nuevo Cliente registrado'
            }

            return render(request, "main/home.html", context)

        else:
            context = {
                'form': form,
                'error': True
            }

            return render(request, "main/register.html", context)

    else:
        form = RegisterClient()

        context = {
            'form': form,
        }

        return render(request, "main/login.html", context)

# Login to the Client
def login_view(request):
    if request.POST:
        form = LoginClient(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(reverse('main:home'))

            else:
                context = {
                    'form': form,
                    'error': True,
                    'error_message': 'Usuario No Valido'
                }

                return render(request, "main/login.html", context)

        else:
            form = LoginClient()
            context = {
                'form': form
            }

            return render(request, "main/login.html", context)

def logout_view(request):
    logout(request)
    return redirect(reverse('main:home'))