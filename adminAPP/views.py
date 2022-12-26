from django.shortcuts import render, redirect, get_object_or_404
import adminAPP.views
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
# serializadores librerias
from rest_framework import viewsets
from .serializers import *
import requests



# HOME

def home(request):
    return render(request, './Home/home.html')


# LOGIN

def login(request):
    return render(request, './registration/login.html')



# Panel principal

def panel(request):
    return render(request, './panel/panelprincipal.html')


# Articulos computacionales
# @login_required
# @permission_required('adminAPP.views.ingresar_art_oficina')
def ingresar_art_computacionales(request):

    data = {
        'form': InsumosComputacionalesForm()
    }
    if request.method == 'POST':
        formulario = InsumosComputacionalesForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "SE HA REGISTRADO EXITOSAMENTE."
        else:
            data['form'] = formulario

    return render(request, './art_computacionales/ingresar.html', data)

# Articulos computacionales
# @login_required
# @permission_required('adminAPP.view_insumo_computacionales')
def listar_art_computacionales(request):
    busqueda = request.GET.get("buscar")
    listar = InsumoComputacion.objects.all()

    if busqueda:
        listar = InsumoComputacion.objects.filter(
            Q(Codigo__icontains=busqueda) |
            Q(Marca__icontains=busqueda) |
            Q(Tipo__icontains=busqueda)
        ).distinct()

    data = {
        'listar': listar,
    }
    return render(request, './art_computacionales/listar.html', data)


# Articulos computacionales
@login_required
@permission_required('adminAPP.change_insumo_computacionales')
def modificar_art_computacionales(request, id):
    insumos_computacion = get_object_or_404(InsumoComputacion, id=id)

    data = {
        'form':InsumosComputacionalesForm(instance=insumos_computacion)
    }
    if request.method == 'POST':
        formulario = InsumosComputacionalesForm(data=request.POST, instance=insumos_computacion)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_art_computacionales")
        data["form"] = formulario

    return render(request, './art_computacionales/modificar.html', data)


# Articulos computacionales
@login_required
# @permission_required('adminAPP.delete_insumo_computacionales')
def eliminar_art_computacionales(request, id):
    eliminar_insumo_comp = get_object_or_404(InsumoComputacion, id=id)
    eliminar_insumo_comp.delete()
    return redirect(to="listar_art_computacionales")


# Articulos Oficina

@permission_required('adminAPP.add_ingresar_art_oficina')
def ingresar_art_oficina(request):

    data = {
        'form': InsumosOficinasForm()
    }
    if request.method == 'POST':
        formulario = InsumosOficinasForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "SE HA REGISTRADO EXITOSAMENTE."
        else:
            data['form'] = formulario

    return render(request, './art_oficina/ingresar.html', data)



# Articulos Oficina

@permission_required('adminAPP.imsmo_oficina.view_insmo_oficina')
def listar_art_oficina(request):
    busqueda = request.GET.get("buscar")
    listar = InsmoOficina.objects.all()

    if busqueda:
        listar = InsmoOficina.objects.filter(
            Q(Codigo__icontains = busqueda) |
            Q(Tipo__icontains=busqueda) |
            Q(Ubicacion__icontains=busqueda)
        ).distinct()

    data = {
        'listar': listar,
    }
    return render(request, './art_oficina/listar.html', data)



# Articulos Oficina

@permission_required('adminAPP.imsmo_oficina.change_insmo_oficina')
def modificar_art_oficina(request, id):
    insumos_oficina = get_object_or_404(InsmoOficina, id=id)

    data = {
        'form':InsumosOficinasForm(instance=insumos_oficina)
    }
    if request.method == 'POST':
        formulario = InsumosOficinasForm(data=request.POST, instance=insumos_oficina)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_art_oficina")
        data["form"] = formulario

    return render(request, './art_oficina/modificar.html', data)



# Articulos Oficina

@permission_required('adminAPP.imsmo_oficina.delete_insmo_oficina')
def eliminar_art_oficina(request, id):
    eliminar_insumo_of = get_object_or_404(InsmoOficina, id=id)
    eliminar_insumo_of.delete()
    return redirect(to="listar_art_oficina")



# Registro Vehiculo

@permission_required('adminAPP.add_registro_vehiculo')
def ingresar_reg_vehiculo(request):

    data = {
        'form': RegistroVehiculosForm()
    }
    if request.method == 'POST':
        formulario = RegistroVehiculosForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "EL VEHICULO SE HA REGISTRADO EXITOSAMENTE."
        else:
            data['form'] = formulario

    return render(request, './reg_vehiculos/ingresar.html', data)



# Registro Vehiculo

@permission_required('adminAPP.view_registro_vehiculo')
def listar_reg_vehiculo(request):
    busqueda = request.GET.get("buscar")
    listar = RegistroVehiculo.objects.all()

    if busqueda:
        listar = RegistroVehiculo.objects.filter(
            Q(Codigo__icontains = busqueda) |
            Q(Tipo__icontains=busqueda) |
            Q(Patente__icontains=busqueda)|
            Q(Numero_de_chasis__icontains=busqueda) |
            Q(Marca__icontains=busqueda) |
            Q(Modelo__icontains=busqueda)
        ).distinct()

    data = {
        'listar': listar,
    }
    return render(request, './reg_vehiculos/listar.html', data)



# Registro Vehiculo

@permission_required('adminAPP.change_registro_vehiculo')
def modificar_reg_vehiculo(request, id):
    registro_vehiculo = get_object_or_404(RegistroVehiculo, id=id)

    data = {
        'form':RegistroVehiculosForm(instance=registro_vehiculo)
    }
    if request.method == 'POST':
        formulario = RegistroVehiculosForm(data=request.POST, instance=registro_vehiculo)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'EL USUARIO SE HA MODIFICADO EXITOSAMENTE.'

        return redirect(to="listar_reg_vehiculo")
        data["form"] = formulario

    return render(request, './reg_vehiculos/modificar.html', data)


# Registro Vehiculo

@permission_required('adminAPP.delete_registro_vehiculo')
def eliminar_reg_vehiculo(request, id):
    eliminar_reg_vehiculo = get_object_or_404(RegistroVehiculo, id=id)
    eliminar_reg_vehiculo.delete()
    return redirect(to="listar_art_oficina")


def ingresar_usuario(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"], permisions=formulario.cleaned_data["user_permissions"])
            login(request)
            messages.success(request, "Te has registrado en forma exitosa")
            return redirect(to="login")
        data["form"] = formulario
    return render(request, './registration/registro.html', data)


# Usuario

@permission_required('adminAPP.view_usuarios')

def listar_usuario(request):
    busqueda = request.GET.get("buscar")
    listar = User.objects.all()

    if busqueda:
        listar = User.objects.filter(
            Q(username__icontains = busqueda) |
            Q(first_name__icontains=busqueda) |
            Q(last_name__icontains=busqueda)|
            Q(email__icontains=busqueda)
        ).distinct()

    data = {
        'listar': listar,
    }

    return render(request, './usuarios/listar.html', data)


# Usuario

@permission_required('adminAPP.change_usuarios')
def modificar_usuario(request, id):
    registro_user = get_object_or_404(User, id=id)

    data = {
        'form':CustomUserCreationForm(instance=registro_user)
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST, instance=registro_user)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_usuario")
        data["form"] = formulario

    return render(request, './usuarios/modificar.html', data)


# Usuario

@permission_required('adminAPP.delete_usuarios')
def eliminar_usuario(request, id):
    eliminar_usuario = get_object_or_404(User, id=id)
    eliminar_usuario.delete()
    return redirect(to="listar_usuario")



# CLASES VISTAS SERIALIZADORES

class InsumoComputacionViewset(viewsets.ModelViewSet):
    queryset = InsumoComputacion.objects.all()
    serializer_class = InsumoComputacionSerializer

class InsmoOficinaViewset(viewsets.ModelViewSet):
    queryset = InsmoOficina.objects.all()
    serializer_class = InsmoOficinaSerializer

class RegistroVehiculoViewset(viewsets.ModelViewSet):
    queryset = RegistroVehiculo.objects.all()
    serializer_class = RegistroVehiculoSerializer


#MOSTRAR DATOS API

def api_artcomputacionales(request):
    solicitud = requests.get('http://127.0.0.1:8000/api/insumos-computacionales/').json()

    context = {
        'solicitud': solicitud,


    }
    return render(request, './art_computacionales/mostrarapi.html', context)





































