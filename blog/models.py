from django.db import models

# Create your models here.

class Producto(models.Model): #Modelo abstracto
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    peso=models.CharField(max_length=50)

    class Meta:
        abstract=True


class Refrigeradora(Producto):
    temperatura_minima=models.CharField(max_length=50)
    pantalla_inteligente=models.CharField(max_length=50)
    volumen=models.CharField(max_length=50)
    marca=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre+'  '+self.peso+'  '+self.marca

class Laptop(Producto):
    cpu=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre+'  '+self.peso+'  '+self.cpu
  
class Prueba(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    peso=models.CharField(max_length=50)
    cpu=models.CharField(max_length=50)