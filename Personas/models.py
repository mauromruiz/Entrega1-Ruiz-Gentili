from django.db import models
from ckeditor.fields import RichTextField
# from django.contrib.auth.models import Persona

class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_creacion = models.DateField(null=True)
    foto_persona = models.ImageField(upload_to='fotos', null=True, blank=True)
    # persona = models.OneToOneField(Persona,on_delete=models.CASCADE)
    descripcion = RichTextField(null=True)

    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido}'