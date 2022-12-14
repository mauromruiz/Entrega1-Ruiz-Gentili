from django.shortcuts import render
from Personas.models import Persona
from Personas.forms import BuscarPersonaFormulario

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return render(request, 'Personas/index.html')

def about(request):
    return render(request, 'Personas/About.html')

class Ver_persona(ListView):
    model = Persona
    template_name = 'Personas/Ver_persona.html'
    
    def get_queryset(self):
        nombre = self.request.GET.get('nombre', '')
        if nombre:
            object_list = self.model.objects.filter(nombre__icontains=nombre)
        else:
            object_list = self.model.objects.all()
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formulario"] = BuscarPersonaFormulario()
        return context

class Crear_persona(LoginRequiredMixin, CreateView):
    model = Persona
    success_url = '/Ver_persona/'
    template_name = 'Personas/Crear_persona.html'
    fields = ['nombre', 'apellido', 'edad', 'fecha_creacion', 'descripcion', 'foto_persona']
    
class Editar_persona(LoginRequiredMixin, UpdateView):
    model = Persona
    success_url = '/Ver_persona/'
    template_name = 'Personas/Editar_persona.html'
    fields = ['nombre', 'apellido', 'edad', 'fecha_creacion', 'descripcion', 'foto_persona']
    
class Eliminar_persona(LoginRequiredMixin, DeleteView):
    model = Persona
    success_url = '/Ver_persona/'
    template_name = 'Personas/Eliminar_persona.html'

class Ver_TodaInformacion(DetailView):
    model = Persona
    template_name = 'Personas/Ver_TodaInformacion.html' 
    