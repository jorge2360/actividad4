from django.shortcuts import render, redirect, get_object_or_404
from .models import Publicacion, EstudiantePublicador, EstudianteAutorizador, Comentario
from .forms import ComentarioForm

def publicaciones(request):
    publicaciones = Publicacion.objects.all()
    publicadores = EstudiantePublicador.objects.all()
    autorizadores = EstudianteAutorizador.objects.all()
    form_com = ComentarioForm()

    if request.method == 'POST' and 'crear_comentario' in request.POST:
        form_com = ComentarioForm(request.POST)
        if form_com.is_valid():
            comentario = form_com.save(commit=False)
            publicacion_id = request.POST.get("publicacion_id")
            comentario.publicacion = get_object_or_404(Publicacion, id=publicacion_id)
            comentario.save()
            return redirect('revista:publicaciones')

    return render(request, "revista/publicaciones.html", {
        "publicaciones": publicaciones,
        "publicadores": publicadores,
        "autorizadores": autorizadores,
        "form_com": form_com
    })
def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    return render(request, "revista/detalle_publicacion.html", {"publicacion": publicacion})