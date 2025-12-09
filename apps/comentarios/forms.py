# apps/comentarios/forms.py
from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        # ¡CORREGIDO! Usamos 'contenido' en lugar de 'texto'
        fields = ['contenido'] 
        
        # Etiquetas personalizadas
        labels = {
            'contenido': 'Tu Comentario',
        }
        # Widgets para personalizar el campo de texto
        widgets = {
            'contenido': forms.Textarea(attrs={
                'rows': 4, 
                'placeholder': 'Escribe tu comentario aquí...'
            }),
        }