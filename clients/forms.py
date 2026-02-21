from django import forms
from django.contrib.auth.password_validation import validate_password

# Register Client
class ContactClient(forms.Form):
    first_name = forms.CharField(max_length=100, label="Nombre")
    email = forms.CharField(max_length=100, label="Email")
    message = forms.CharField(label="Mensaje", widget=forms.Textarea)

    def cleaned_name(self):
        name = self.cleaned_data.get("name")

        if len(name) < 6:
            raise forms.ValidationError("El Nombre debe tener al Menos 6 Caracteres")

class RegisterClient(forms.Form):
    username = forms.CharField(max_length=50, label="Nombre de Usuario")
    first_name = forms.CharField(max_length=100, label="Nombre")
    last_name = forms.CharField(max_length=100, label="Apellido")
    email = forms.CharField(max_length=100, label="Email")
    phone = forms.IntegerField(label="Numero de Telefono")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita la Contraseña", widget=forms.PasswordInput)

    def cleaned_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 != password2 and password1 != '':
            raise forms.ValidationError('Las Constraseñas No Coinciden')

        if password2 != '':
            validate_password(password2)

# Login Client
class LoginClient(forms.Form):
    username = forms.CharField(max_length=100, label="Nombre de Usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput())