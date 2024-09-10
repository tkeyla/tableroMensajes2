
from mensajes.models import Mensaje

m1 = Mensaje(texto='hola', remitente='dario')
m2 = Mensaje(texto='me duele la cabeza', remitente='lolo')
m3 = Mensaje(texto='quiero cocinar galletitas con chips de chocolate', remitente='pedro')
m4 = Mensaje(texto='si me saco 8 de nuevo lloro', remitente='moria')
m5 = Mensaje(texto='tengo que estudiar para el final de redes aaa', destinatario='fabio')
m6 = Mensaje(texto='its race weeeek', destinatario='franco')
m7 = Mensaje(texto='toca estudiar', remitente='vale')
m8 = Mensaje(texto='tengo hambreeeee', destinatario='mamá')
m9 = Mensaje(texto='empezó el partidooooooo', remitente='vale')
m10 = Mensaje(texto='buenas buenas', remitente='nina')
mensajes = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10]
for m in mensajes:
    m.save()