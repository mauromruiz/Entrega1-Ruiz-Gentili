from django import forms
from ckeditor.fields import RichTextFormField

class PersonaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    fecha_creacion = forms.DateField(required=False)
    descripcion = RichTextFormField(required=False)
    
    
class BuscarPersonaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)