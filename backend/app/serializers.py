from rest_framework import serializers

from .models import *

class RestauranteSerializerCrear(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = ['nombre','codigo']
        read_only_fields = ['codigo']

class RestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = ['id','nombre','codigo','fecha_creacion']
        
class RestauranteSerializerModNombre(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = ['nombre']
        
class EstacionesSerializerCrear(serializers.ModelSerializer):
    class Meta:
        model = Estacion_Trabajo
        fields = ['restaurante','nombre']