from django.db import models
from django.contrib.auth.models import AbstractUser



tipo_computacion = [
    ["Monitor", "Monitor"],
    ["Desktop", "Desktop"],
    ["Laptop", "Laptop"],
    ["Mouse", "Mouse"],
    ["Teclados", "Teclados"],
    ["Impresoras", "Impresoras"],
    ["perisfericos", "perisfericos"],
    ["Otros", "Otros"],
]

tipo_artoficina = [
    ["Papeleria", "Papeleria"],
    ["Muebleria", "Muebleria"],
    ["Sillas", "Sillas"],
    ["Lapices", "Lapices"],
    ["Otros", "Otros"],

]


tipo_vehiculo = [
    ["Sedan", "Sedan"],
    ["Hachback", "Hachback"],
    ["Camioneta", "Camioneta"],
    ["Furgoneta", "Furgoneta"],
]

# tipo_usuario = [
#     ["Administrador", "Administrador"],
#     ["Insumos Computacionales", "Insumos Computacionales"],
#     ["Insumos Oficina", "Insumos Oficina"],
#     ["Registro Vehiculos", "Registro Vehiculos"],
# ]

class InsumoComputacion(models.Model):
    Codigo = models.IntegerField(max_length=50, unique=True)
    Tipo = models.CharField(max_length=100, choices=tipo_computacion)
    Marca = models.CharField(max_length=100)
    Fecha_de_adquisicion = models.DateField(max_length=100)
    Stock = models.IntegerField(max_length=50)
    Descripcion = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.Tipo


class InsmoOficina(models.Model):
    Codigo = models.IntegerField(unique=True)
    Tipo= models.CharField(max_length=100, choices=tipo_artoficina)
    Ubicacion = models.CharField(max_length=100)
    Stock = models.IntegerField()
    Descripcion = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.Tipo


class RegistroVehiculo(models.Model):
    Codigo = models.IntegerField(max_length=50, unique=True)
    Tipo = models.CharField(max_length=100, choices=tipo_vehiculo)
    Patente = models.CharField(max_length=100, unique=True)
    Numero_de_chasis = models.CharField(max_length=50, unique=True)
    Marca = models.CharField(max_length=100)
    Modelo = models.CharField(max_length=100)
    Ultima_revision = models.DateField(max_length=100)
    Proxima_revision = models.DateField(max_length=100)
    Observaciones = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.patente

# class Usuario(AbstractUser):
#     pass

# class Usuarios(models.Model):
#     Perfil = models.CharField(max_length=100, choices=tipo_usuario, unique=True)
#     Nombre_de_usuario = models.CharField(max_length=100)
#     Nombre_completo = models.CharField(max_length=100)
#     Correo_electronico = models.EmailField(max_length=100)
#
#     def __str__(self):
#         return self.perfil

