
from django.db import models
from django.forms import CharField

# Create your models here.




class Mama(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    fecha_de_nacimiento= models.CharField(max_length=10)
    residencia=models.CharField(max_length=50)
    hijos= models.IntegerField()

class Hermano_mayor(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    fecha_de_nacimiento= models.CharField(max_length=50)
    residencia=models.CharField(max_length=20)
    correo= models.EmailField()
    estudio= models.CharField(max_length=20)

class Esposo(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    fecha_de_nacimiento= models.CharField(max_length=50)
    residencia= models.CharField(max_length=20)
    profesion= models.CharField(max_length=50)