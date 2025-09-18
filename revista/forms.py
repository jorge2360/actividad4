from django import forms
from .models import Publicacion, Comentario

# Formulario para crear/editar publicaciones (administrador)
class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'contenido']

# Formulario para comentar publicaciones (estudiantes)
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nombre_estudiante', 'contenido']
