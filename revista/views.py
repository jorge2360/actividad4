from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy

from .models import Publicacion, EstudiantePublicador, EstudianteAutorizador
from .forms import ComentarioForm, EstudiantePublicadorForm, EstudianteAutorizadorForm, PublicacionForm

def publicaciones(request):
    publicaciones = Publicacion.objects.all()
    publicadores = EstudiantePublicador.objects.all()
    autorizadores = EstudianteAutorizador.objects.all()

    # Formulario de nueva publicación
    if request.method == 'POST' and 'crear_publicacion' in request.POST:
        form_pub = PublicacionForm(request.POST)
        if form_pub.is_valid():
            nueva_pub = form_pub.save(commit=False)
            nueva_pub.save()
            return redirect('revista:publicaciones')
    else:
        form_pub = PublicacionForm()

    # Formulario de comentario
    if request.method == 'POST' and 'crear_comentario' in request.POST:
        form_com = ComentarioForm(request.POST)
        if form_com.is_valid():
            comentario = form_com.save(commit=False)
            publicacion_id = request.POST.get("publicacion_id")
            comentario.publicacion = get_object_or_404(Publicacion, id=publicacion_id)
            comentario.save()
            return redirect('revista:publicaciones')
    else:
        form_com = ComentarioForm()

    return render(request, "revista/publicaciones.html", {
        "publicaciones": publicaciones,
        "publicadores": publicadores,
        "autorizadores": autorizadores,
        "form_pub": form_pub,
        "form_com": form_com
    })


def agregar_publicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('revista:publicaciones')
    else:
        form = PublicacionForm()
    return render(request, 'revista/agregar_publicacion.html', {'form': form})


def estudiantes(request):
    estudiantes = EstudiantePublicador.objects.all()

    if request.method == 'POST':
        form_pub = EstudiantePublicadorForm(request.POST)
        if form_pub.is_valid():
            form_pub.save()
            return redirect('revista:estudiantes')
    else:
        form_pub = EstudiantePublicadorForm()

    return render(request, "revista/estudiantes.html", {
        "estudiantes": estudiantes,
        "form_pub": form_pub
    })


def administradores(request):
    administradores = EstudianteAutorizador.objects.all()

    if request.method == 'POST':
        form_aut = EstudianteAutorizadorForm(request.POST)
        if form_aut.is_valid():
            form_aut.save()
            return redirect('revista:administradores')
    else:
        form_aut = EstudianteAutorizadorForm()

    return render(request, "revista/administradores.html", {
        "administradores": administradores,
        "form_aut": form_aut
    })


def agregar_publicador(request):
    if request.method == 'POST':
        form = EstudiantePublicadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('revista:estudiantes')
    else:
        form = EstudiantePublicadorForm()
    return render(request, 'revista/agregar_publicador.html', {'form': form})


def agregar_autorizador(request):
    if request.method == 'POST':
        form = EstudianteAutorizadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('revista:administradores')
    else:
        form = EstudianteAutorizadorForm()
    return render(request, 'revista/agregar_autorizador.html', {'form': form})

# DETAIL y UPDATE VIEWS

# --- Estudiantes ---
class EstudianteDetailView(DetailView):
    model = EstudiantePublicador
    template_name = "revista/estudiante_detail.html"
    context_object_name = "estudiante"


class EstudianteUpdateView(UpdateView):
    model = EstudiantePublicador
    form_class = EstudiantePublicadorForm
    template_name = "revista/estudiante_form.html"
    success_url = reverse_lazy("revista:estudiantes")


# --- Administradores ---
class AdministradorDetailView(DetailView):
    model = EstudianteAutorizador
    template_name = "revista/administrador_detail.html"
    context_object_name = "administrador"


class AdministradorUpdateView(UpdateView):
    model = EstudianteAutorizador
    form_class = EstudianteAutorizadorForm
    template_name = "revista/administrador_form.html"
    success_url = reverse_lazy("revista:administradores")


# --- Publicaciones ---
class PublicacionDetailView(DetailView):
    model = Publicacion
    template_name = "revista/publicacion_detail.html"
    context_object_name = "publicacion"


class PublicacionUpdateView(UpdateView):
    model = Publicacion
    form_class = PublicacionForm
    template_name = "revista/publicacion_form.html"
    success_url = reverse_lazy("revista:publicaciones")
