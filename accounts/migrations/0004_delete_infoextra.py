# Generated by Django 4.1.2 on 2022-12-14 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_infoextra_remove_extensionusuario_nacionalidad'),
    ]

    operations = [
        migrations.DeleteModel(
            name='InfoExtra',
        ),
    ]
