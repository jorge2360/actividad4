from django import forms
from .models import Comentario
from .models import EstudiantePublicador, EstudianteAutorizador, Publicacion

class EstudiantePublicadorForm(forms.ModelForm):
    class Meta:
        model = EstudiantePublicador
        fields = ['nombre', 'correo', 'carrera']

class EstudianteAutorizadorForm(forms.ModelForm):
    class Meta:
        model = EstudianteAutorizador
        fields = ['nombre', 'correo', 'departamento']

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'contenido', 'publicador', 'autorizador']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nombre_estudiante', 'contenido']