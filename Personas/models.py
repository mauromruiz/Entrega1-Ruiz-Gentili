from django.db import models
from ckeditor.fields import RichTextField

class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_creacion = models.DateField(null=True)
    descripcion = RichTextField(null=True)

    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido}'