from django.shortcuts import render
from Personas.models import Persona

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def index(request):
    return render(request, 'Personas/index.html')

def about(request):
    return render(request, 'Personas/About.html')

class Ver_persona(ListView):
    model = Persona
    template_name = 'Personas/Ver_persona.html'

class Crear_persona(CreateView):
    model = Persona
    success_url = '/Ver_persona/'
    template_name = 'Personas/Crear_persona.html'
    fields = ['nombre', 'apellido', 'edad', 'fecha_creacion']
    
class Editar_persona(UpdateView):
    model = Persona
    success_url = '/Ver_persona/'
    template_name = 'Personas/Editar_persona.html'
    fields = ['nombre', 'apellido', 'edad', 'fecha_creacion']
    
class Eliminar_persona(DeleteView):
    model = Persona
    success_url = '/Ver_persona/'
    template_name = 'Personas/Eliminar_persona.html'
    