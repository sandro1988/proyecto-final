from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    def __str__(self):
      return f"{self.nombre}, {self.numero_pasaporte}, {self.direccion}, {self.id}"

      #------

      # Create your models here.
class Coche(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    anio = models.IntegerField()
    km = models.IntegerField()
    def __str__(self):
      return f"{self.marca}, {self.modelo}, {self.anio}, {self.km}"