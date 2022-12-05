from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class InsumosComputacionalesForm(forms.ModelForm):

    class Meta:
        model = InsumoComputacion
        fields = '__all__'

#
class InsumosOficinasForm(forms.ModelForm):

    class Meta:
        model = InsmoOficina
        fields = '__all__'

class RegistroVehiculosForm(forms.ModelForm):

    class Meta:
        model = RegistroVehiculo
        fields = '__all__'



# class RegistroUsuariosForm(forms.ModelForm):
#
#     class Meta:
#         model = Usuarios
#         fields = '__all__'



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2','groups', 'user_permissions', 'date_joined', 'last_login']
