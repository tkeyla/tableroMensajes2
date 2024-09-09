from django.shortcuts import render
from django.views.generic import ListView
from .models import Mensaje
from .templates import *

def principal(request):
    return render (request, 'home.html')

def ver_enviados(request):
    mensajes = Mensaje.objects.filter(remitente='keyla')
    return render(request, 'verMsjsEnviados.html', {'mensajes': mensajes})

def ver_recibidos(request):
    mensajes = Mensaje.objects.filter(destinatario='keyla')
    return render(request, 'verMsjsRecibidos.html', {'mensajes': mensajes})

class MensajeListView(ListView):
    model = Mensaje
    template_name = 'eliminarMsjs.html'
    context_object_name = 'mensajes'