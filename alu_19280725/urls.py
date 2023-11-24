from django.urls import path

# from .views import hola, demo
from . import views

urlpatterns = [
    path('', views.index),
    path('contactos/', views.contactos),
    path('mensajes/<int:id_contacto>/', views.mensajes, name='mensajes'),
    path('crear_mensaje/', views.crear_mensaje, name='crear_mensaje'),
]