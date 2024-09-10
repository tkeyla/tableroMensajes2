from django.shortcuts import render, redirect
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

def eliminar_mensajes(request):
    id_seleccionados  = str (request.GET.get('mensajes_seleccionados'))
    id_seleccionados = id_seleccionados.split(',')
    id_seleccionados = [id for id in id_seleccionados if id.isdigit()]
    Mensaje.objects.filter(id__in=id_seleccionados).delete()
    return redirect('seleccionarMsjs')
