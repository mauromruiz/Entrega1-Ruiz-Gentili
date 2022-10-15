from django.urls import path
from Personas import views

urlpatterns = [
    path('', views.index),
    path('Ver_persona/', views.ver_persona),
    path('Crear_persona/<str:nombre>/<str:apellido>/', views.crear_persona),
]