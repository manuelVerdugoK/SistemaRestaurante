from django.urls import path
from .views import crearRestaurante,listarRestaurantes,cambiarNombreRestaurante,eliminarRestaurante
from .views import crearEstacion
urlpatterns = [
    path('restaurante/crear-restaurante/', crearRestaurante, name='crear_restaurante'),
    path('restaurante/listar-restaurante/', listarRestaurantes, name='listar_restaurante'),
    path('restaurante/<int:id>/cambiar-nombre/', cambiarNombreRestaurante, name='cambiar-nombre-restaurante'),
    path('restaurante/<int:id>/eliminar-restaurante/', eliminarRestaurante, name='eliminar-restaurante'),
    
    path('estaciones/crear-estacion/', crearEstacion, name='crear_estacion'),
]