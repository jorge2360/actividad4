from django.db import models

# Estudiantes que publican noticias
class EstudiantePublicador(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    carrera = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


# Estudiantes que autorizan publicaciones
class EstudianteAutorizador(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    departamento = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


# Publicaciones
class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateField(auto_now_add=True)

    publicador = models.ForeignKey(EstudiantePublicador, on_delete=models.CASCADE)
    autorizador = models.ForeignKey(EstudianteAutorizador, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name="comentarios")
    nombre_estudiante = models.CharField(max_length=100)  # quien comenta
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre_estudiante} - {self.publicacion.titulo}"