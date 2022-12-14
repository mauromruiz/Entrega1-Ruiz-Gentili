from django.urls import path
from Personas import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('About/', views.about, name='About'),
    path('Ver_persona/', views.Ver_persona.as_view(), name='Ver_persona'),
    path('Crear_persona/', views.Crear_persona.as_view(), name='Crear_persona'),
    path('Editar_persona/<int:pk>/', views.Editar_persona.as_view(), name='Editar_persona'),
    path('Eliminar_persona/<int:pk>/', views.Eliminar_persona.as_view(), name='Eliminar_persona'),
    path('Ver_TodaInformacion/<int:pk>/', views.Ver_TodaInformacion.as_view(), name='Ver_TodaInformacion'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)