# Generated by Django 4.1.2 on 2022-11-13 05:23

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Personas', '0002_alter_persona_fecha_creacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='descripcion',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
