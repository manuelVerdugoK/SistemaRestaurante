from django.db import models
import string
import random

class Restaurante (models.Model):
    nombre = models.CharField(max_length=20, null=False, unique=True)
    codigo = models.CharField(max_length=10, null=False, unique=True)
    fecha_creacion = models.TimeField(auto_now_add=True)
    
    def codigo_restaurante(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    
    def save(self, *args, **kwargs):
        if not self.codigo:
            self.codigo = self.codigo_restaurante()
        super(Restaurante, self).save(*args, **kwargs)

class Estacion_Trabajo (models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20,null=False)
    
class Trabajador (models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20)
    correo = models.EmailField(max_length=50, unique=True)
    estacion = models.ForeignKey(Estacion_Trabajo, on_delete=models.CASCADE)

class Mesa (models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    numero = models.IntegerField(null=False)
    
class Producto(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    estacion = models.ForeignKey(Estacion_Trabajo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255,null=False)
    precio = models.IntegerField(null=False)
    fecha_creacion = models.DateField(null=False)
    
    
class EstadoOrden (models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20)
    
class EstadoProductosOrden (models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20)
    
class EstadoBoleta (models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20)
       
class Orden (models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    estado = models.ForeignKey(EstadoOrden,on_delete=models.CASCADE)

class Orden_Productos (models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    orden = models.ForeignKey(Orden,on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    estado = models.ForeignKey(EstadoProductosOrden,on_delete=models.CASCADE)
    
class Boleta (models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    orden = models.ForeignKey(Orden,on_delete=models.CASCADE)
    productos = models.ForeignKey(Orden_Productos, on_delete=models.CASCADE)
    subtotal = models.IntegerField(null=False)
    total = models.IntegerField(null=False)
    estado = models.ForeignKey(EstadoBoleta,on_delete=models.CASCADE)
    