from .models import *
from rest_framework import serializers

class InsumoComputacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsumoComputacion
        fields = '__all__'


class InsmoOficinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsmoOficina
        fields = '__all__'


class RegistroVehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroVehiculo
        fields = '__all__'
