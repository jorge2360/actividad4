from django.shortcuts import render, redirect, get_object_or_404
from .models import Publicacion, EstudiantePublicador, EstudianteAutorizador
from .forms import ComentarioForm
from .forms import EstudiantePublicadorForm, EstudianteAutorizadorForm

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

def estudiantes(request):
    publicadores = EstudiantePublicador.objects.all()
    form = EstudiantePublicadorForm()

    if request.method == "POST" and "crear_publicador" in request.POST:
        form = EstudiantePublicadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("revista:estudiantes")

    return render(request, "revista/estudiantes.html", {
        "publicadores": publicadores,
        "form": form
    })


def administradores(request):
    autorizadores = EstudianteAutorizador.objects.all()
    form = EstudianteAutorizadorForm()

    if request.method == "POST" and "crear_autorizador" in request.POST:
        form = EstudianteAutorizadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("revista:administradores")

    return render(request, "revista/administradores.html", {
        "autorizadores": autorizadores,
        "form": form
    })