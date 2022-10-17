from datetime import datetime
from django.shortcuts import render, redirect
from Personas.models import Persona
from Personas.forms import BuscarPersonaFormulario, PersonaFormulario

def index(request):
    return render(request, 'Personas/index.html')

def about(request):
    return render(request, 'Personas/About.html')

def ver_persona (request):
    
    nombre = request.GET.get('nombre', None)
    
    if nombre:
        personas = Persona.objects.filter(nombre__icontains=nombre)
    else:
        personas = Persona.objects.all()
    
    formulario = BuscarPersonaFormulario()
    
    return render(request, 'Personas/Ver_persona.html', {'Personas': personas, 'formulario': formulario})

def crear_persona (request):
    
    if request.method == 'POST':
        
        formulario = PersonaFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            
            nombre = data['nombre']
            apellido = data['apellido']
            edad = data['edad']
            fecha_creacion = data['fecha_creacion'] or datetime.now()
            
            persona = Persona(nombre=nombre, apellido=apellido, edad=edad, fecha_creacion=fecha_creacion)
            persona.save()
        
        return redirect('Ver_persona')
    
    formulario = PersonaFormulario()
    
    return render(request, 'Personas/Crear_persona.html', {'formulario': formulario})