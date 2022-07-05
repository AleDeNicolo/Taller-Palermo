from django.db import models

# Create your models here.
class Service(models.Model):
    nombre = models.CharField(max_length=40)
    chasis = models.IntegerField()

    def __str__(self) -> str:
        return self.nombre+""+str(self.chasis)

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.nombre+" "+self.apellido

class Mecanicos (models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    especialidad = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.nombre+" "+str(self.especialidad)
 
class Entregable(models.Model):
    nombre = models.CharField(max_length=40)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()
