# Generated by Django 4.1.2 on 2022-12-13 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='extensionusuario',
            name='nacionalidad',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
