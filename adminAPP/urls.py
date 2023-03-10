from django.urls import path, include
from adminAPP.views import *
from rest_framework import  routers

#rutas Serializador

router = routers.DefaultRouter()
router.register('insumos-computacionales', InsumoComputacionViewset)
router.register('insumos-oficina', InsmoOficinaViewset)
router.register('registro-vehiculos', RegistroVehiculoViewset)


urlpatterns = [
    # HOME
    path('',home, name="home"),
    # LOGIN
    path('login/', login, name="login"),
    # Panel principal
    path('panel/', panel, name="panel"),

    # Articulos computacionales
    path('listar_art_computacionales/', listar_art_computacionales, name="listar_art_computacionales"),
    path('ingresar_art_computacionales/', ingresar_art_computacionales, name="ingresar_art_computacionales"),
    path('modificar_art_computacionales/<id>/', modificar_art_computacionales, name='modificar_art_computacionales'),
    path('eliminar_art_computacionales/<id>/', eliminar_art_computacionales, name='eliminar_art_computacionales'),
    path('api_artcomputacionales/', api_artcomputacionales, name='api_artcomputacionales'),
    path('json_artcomputacionales/', json_artcomputacionales, name='json_artcomputacionales'),

    # Articulos Oficina
    path('listar_art_oficina/', listar_art_oficina, name="listar_art_oficina"),
    path('ingresar_art_oficina/', ingresar_art_oficina, name="ingresar_art_oficina"),
    path('modificar_art_oficina/<id>/', modificar_art_oficina, name='modificar_art_oficina'),
    path('eliminar_art_oficina/<id>/', eliminar_art_oficina, name='eliminar_art_oficina'),
    path('api_artoficina/', api_artoficina, name='api_artoficina'),
    path('json_artoficina/', json_artoficina, name='json_artoficina'),


    # Registro Vehiculo
    path('ingresar_reg_vehiculo/', ingresar_reg_vehiculo, name="ingresar_reg_vehiculo"),
    path('listar_reg_vehiculo/', listar_reg_vehiculo, name="listar_reg_vehiculo"),
    path('modificar_reg_vehiculo/<id>/', modificar_reg_vehiculo, name='modificar_reg_vehiculo'),
    path('eliminar_reg_vehiculo/<id>/', eliminar_reg_vehiculo, name='eliminar_reg_vehiculo'),
    path('api_regvehiculos/', api_regvehiculos, name='api_regvehiculos'),
    path('json_regvehiculos/', json_regvehiculos, name='json_regvehiculos'),


    # Usuario
    path('ingresar_usuario/', ingresar_usuario, name="ingresar_usuario"),
    path('listar_usuario/', listar_usuario, name="listar_usuario"),
    path('modificar_usuario/<id>/', modificar_usuario, name='modificar_usuario'),
    path('eliminar_usuario/<id>/', eliminar_usuario, name='eliminar_usuario'),

    # PATH para la API


    path('api/', include(router.urls)),

]