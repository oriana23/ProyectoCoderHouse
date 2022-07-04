from multiprocessing import context
from django.http import HttpResponse
from django.template import Context, Template, loader


def saludo(request):
    return HttpResponse("Hola")


def primer_template(self):
    
    nombre="Oriana"
    apellido="Ramirez"

    diccionario={"nombre":nombre, "apellido":apellido}
    
    plantilla=loader.get_template('template.html')
    

    documento=plantilla.render(diccionario)
    return HttpResponse(documento)

