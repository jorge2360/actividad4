from django.contrib import admin
from .models import EstudiantePublicador, EstudianteAutorizador, Publicacion, Comentario


@admin.register(EstudiantePublicador)
class EstudiantePublicadorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "correo", "carrera")
    search_fields = ("nombre", "correo", "carrera")


@admin.register(EstudianteAutorizador)
class EstudianteAutorizadorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "correo", "departamento")
    search_fields = ("nombre", "correo", "departamento")


class ComentarioInline(admin.TabularInline):
    model = Comentario
    extra = 1
    fields = ("nombre_estudiante", "contenido", "fecha_creacion")
    readonly_fields = ("fecha_creacion",)


@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ("titulo", "fecha_publicacion", "publicador", "autorizador")
    list_filter = ("fecha_publicacion", "publicador", "autorizador")
    search_fields = ("titulo", "contenido")
    inlines = [ComentarioInline]


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("publicacion", "nombre_estudiante", "contenido", "fecha_creacion")
    list_filter = ("fecha_creacion", "publicacion")
    search_fields = ("nombre_estudiante", "contenido")
    readonly_fields = ("fecha_creacion",)
