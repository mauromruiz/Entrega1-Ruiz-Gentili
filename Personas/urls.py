from django.urls import path
from Personas import views

urlpatterns = [
    path('', views.index, name='index'),
    path('About/', views.about, name='About'),
    path('Ver_persona/', views.ver_persona, name='Ver_persona'),
    path('Crear_persona/', views.crear_persona, name='Crear_persona'),
]