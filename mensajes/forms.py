from django import forms

class MensajeForm(forms.Form):
    destinatario = forms.CharField(label='Destinatario:', max_length=25)
    mensaje = forms.CharField(label='Mensaje:', widget=forms.Textarea)
    

