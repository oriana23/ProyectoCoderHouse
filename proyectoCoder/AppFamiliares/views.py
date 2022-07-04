from django.shortcuts import render
from AppFamiliares.models import Esposo, Mama, Hermano_mayor, Esposo
from django.http import HttpResponse
from django.template import Template, loader

# Create your views here.

def bienvenida(request):
    curso="Python"
    alumna="Oriana Ramirez"
    desafio="Creando mi primer MTV"

    datos={'curso': curso, 'alumna': alumna, 'desafio': desafio}

    plantilla=loader.get_template('template.html')
    documento=plantilla.render(datos)
    return HttpResponse(documento)


def mama(self):
    mama=Mama(nombre="Marisol", apellido="Ramirez", fecha_de_nacimiento= "08/08/1970", residencia= "Chile", hijos=3)
    mama.save()
    informacion= f"Estos son los datos de mi Mama: <br> Nombre: {mama.nombre} <br> Apellido: {mama.apellido} <br> Fecha de nacimiento:{mama.fecha_de_nacimiento} <br> Residencia: {mama.residencia} <br> Hijos: {mama.hijos}"
    return HttpResponse(informacion)

def hermano_mayor(self):
    hermano_mayor=Hermano_mayor(nombre="Yerson", apellido="Ramirez", fecha_de_nacimiento="26/09/1994", residencia="Chile", correo="yersonramirez@gmail.com", estudio="Odontologia")
    hermano_mayor.save()
    datos= f"Informacion de mi hermano: <br> Nombre{hermano_mayor.nombre} <br> Apellido: {hermano_mayor.apellido} <br> Fecha de nacimiento: {hermano_mayor.fecha_de_nacimiento} <br> Residencia: {hermano_mayor.residencia} <br> Correo: {hermano_mayor.correo} <br> Estudio: {hermano_mayor.estudio}"
    return HttpResponse(datos)

def esposo(self):
    esposo=Esposo(nombre="Matias", apellido="Catrina", fecha_de_nacimiento="25/11/1994", residencia="Argentina", profesion="DeVops")
    esposo.save()
    datos=f"Informacion de mi Esposo: <br> Nombre: {esposo.nombre} <br> Apellido: {esposo.apellido} <br> Fecha de nacimiento: {esposo.fecha_de_nacimiento} <br> Residencia: {esposo.residencia} <br> Profesion: {esposo.profesion}"
    return HttpResponse(datos)
