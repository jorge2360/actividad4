from django.shortcuts import render
from .models import EstudiantePublicador, EstudianteAutorizador, Publicacion

def publicaciones(request):
    publicaciones = Publicacion.objects.all()
    publicadores = EstudiantePublicador.objects.all()
    autorizadores = EstudianteAutorizador.objects.all()
    return render(request, 'revista/publicaciones.html', {
        'publicaciones': publicaciones,
        'publicadores': publicadores,
        'autorizadores': autorizadores
    })
