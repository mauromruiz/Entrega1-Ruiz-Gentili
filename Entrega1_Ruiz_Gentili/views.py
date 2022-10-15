from http.client import HTTPResponse
from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
import random
from Personas.models import Persona

def Pagina1 (request):
    
    personas = Persona.objects.all()
    
    template = loader.get_template('Pagina1.html')
    template_renderizado = template.render({'Personas': personas})
    
    return HttpResponse(template_renderizado)

def Pagina2 (request,nombre,apellido):
    
    persona = Persona(nombre=nombre, apellido=apellido, edad=random.randrange(15,80), fecha_creacion=datetime.now())
    persona.save()
    template = loader.get_template('Pagina2.html')
    template_renderizado = template.render({'persona': persona})
    
    return HttpResponse(template_renderizado)