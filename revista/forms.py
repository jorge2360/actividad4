from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nombre_estudiante', 'contenido']
        widgets = {
            'nombre_estudiante': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Escribe tu comentario...'}),
        }
