# Generated by Django 4.1.2 on 2022-12-14 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personas', '0003_persona_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='foto_persona',
            field=models.ImageField(blank=True, null=True, upload_to='fotos'),
        ),
    ]