from django import forms
from .models import Comentario
from .models import EstudiantePublicador, EstudianteAutorizador

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nombre_estudiante', 'contenido']
        widgets = {
            'nombre_estudiante': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Escribe tu comentario...'}),
        }
class EstudiantePublicadorForm(forms.ModelForm):
    class Meta:
        model = EstudiantePublicador
        fields = ['nombre', 'correo', 'carrera']

class EstudianteAutorizadorForm(forms.ModelForm):
    class Meta:
        model = EstudianteAutorizador
        fields = ['nombre', 'correo', 'departamento']