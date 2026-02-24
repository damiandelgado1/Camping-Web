from django.contrib import admin
from django.urls import path
from clients.views import register_view, login_view, logout_view

app_name = "clients"

urlpatterns = [
    path('register/', register_view, name="register"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('admin/', admin.site.urls),
]