from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Restaurante
from .serializers import RestauranteSerializerCrear,RestauranteSerializer,RestauranteSerializerModNombre
from .serializers import EstacionesSerializerCrear
# FUNCIONES PARA RESTAURANTE #

@api_view(['POST'])
def crearRestaurante(request):
    serializer = RestauranteSerializerCrear(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listarRestaurantes(request):
    restaurantes = Restaurante.objects.all()
    serializer = RestauranteSerializer(restaurantes, many=True)
    return Response(serializer.data, status = status.HTTP_200_OK)
    
@api_view(['PUT'])
def cambiarNombreRestaurante(request, id):
    try:    
        restaurante = Restaurante.objects.get(id=id)
    except Restaurante.DoesNotExist:
        return Response({"error": "Restaurante no encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = RestauranteSerializerModNombre(restaurante, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def eliminarRestaurante(request,id):
    try:
        restaurante = Restaurante.objects.get(id=id)
    except Restaurante.DoesNotExist:
        return Response({"error": "Restaurante no encontrado"}, status=status.HTTP_404_NOT_FOUND)
    restaurante.delete()
    return Response({"message": "El restaurante fue eliminado exitosamente."}, status=status.HTTP_200_OK)

# FUNCIONES PARA ESTACIONES #

@api_view(['POST'])
def crearEstacion(request):
    serializer = EstacionesSerializerCrear(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)