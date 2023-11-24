from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Contactos, Mensajes
from .forms import CrearMensaje

# Create your views here.
def index(request):
    mensajes = Mensajes.objects.all()
    contactos = Contactos.objects.all()
    return render(request, 'index.html', {'mensajes': mensajes, 'contactos': contactos, 'contacto': False, 'ajax_contacto': "false"})

def contactos(request):
    mensajes = Mensajes.objects.all()
    contactos = Contactos.objects.all()
    return render(request, 'index.html', {'contactos': contactos, 'mensajes': mensajes})

def mensajes(request, id_contacto):
    contacto = Contactos.objects.get(id = id_contacto)
    mensajes = Mensajes.objects.all()
    contactos = Contactos.objects.all()
    return render(request, 'index.html', {'mensajes': mensajes, 'contactos': contactos, 'id_contacto': id_contacto, 'contacto': contacto, 'formulario': CrearMensaje()})

def crear_mensaje(request):

    if(request.method == 'POST'):
        Mensajes.objects.create(contenido=request.POST['contenido'],contacto_id=request.POST['contacto'],status=1)
        ultimo_mensaje = Mensajes.objects.last().to_dict()
        # Devuelve el contenido del último mensaje en la respuesta JSON
        return JsonResponse({'mensaje': ultimo_mensaje})
