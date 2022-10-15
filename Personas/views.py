from http.client import HTTPResponse
from datetime import datetime
from django.shortcuts import render
import random
from Personas.models import Persona

def ver_persona (request):
    
    personas = Persona.objects.all()
    return render(request, 'Personas/Ver_persona.html', {'Personas': personas})

def crear_persona (request,nombre,apellido):
    
    persona = Persona(nombre=nombre, apellido=apellido, edad=random.randrange(15,80), fecha_creacion=datetime.now())
    persona.save()
    return render(request, 'Personas/Crear_persona.html', {'persona': persona})

def index(request):
    return render(request, 'Personas/index.html')