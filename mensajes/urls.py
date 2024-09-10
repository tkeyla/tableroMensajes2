from django.urls import path
from .import views

urlpatterns = [
    path('',views.principal, name='home'),
    path('enviados', views.ver_enviados, name='verMsjsEnviados'),
    path('recibidos', views.ver_recibidos, name='verMsjsRecibidos'),
    path('seleccionarmensajes', views.MensajeListView.as_view(), name='seleccionarMsjs'),
    path('eliminarmensajes', views.eliminar_mensajes, name='eliminarMsjs'),
    path('crearmensaje', views.crear_mensaje, name='crearMensaje')
]