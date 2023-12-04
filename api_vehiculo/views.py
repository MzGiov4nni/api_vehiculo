from django.shortcuts import render

# Create your views here.
from .serializer import vehiculo_Serializer
from .models import Registro_vehiculo
from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.response import Response

@api_view(['GET'])
def Listar_vehiculo(request):
    registro_vehiculo = Registro_vehiculo.objects.all()
    serializer = vehiculo_Serializer(registro_vehiculo, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def Detalle_vehiculo(request, pk):
    registro_vehiculo = Registro_vehiculo.objects.get(id=pk)
    serializer = vehiculo_Serializer(registro_vehiculo, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def Registro_vehi(request):
    serializer = vehiculo_Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)


@api_view(['PUT'])
def Actualizar_vehiculo(request, pk):
    registro_vehiculo = Registro_vehiculo.objects.get(id=pk)
    serializer = vehiculo_Serializer(instance=registro_vehiculo, data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)


@api_view(['DELETE'])
def Eliminar_vehiculo(request, pk):
    registro_cliente = Registro_vehiculo.objects.get(id=pk)
    registro_cliente.delete()

    return Response('Eliminado')