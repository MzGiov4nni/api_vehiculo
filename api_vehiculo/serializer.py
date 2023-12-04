from rest_framework import serializers
from .models import Registro_vehiculo

class vehiculo_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Registro_vehiculo
        fields='__all__'