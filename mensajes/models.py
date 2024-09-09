from django.db import models

class Mensaje(models.Model):
    texto = models.TextField(default='hola')
    remitente = models.CharField(max_length=25, default='keyla')
    destinatario = models.CharField(max_length=25, default='keyla')
    fecha_y_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.texto

