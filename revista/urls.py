from django.urls import path
from . import views
app_name = 'revista'
urlpatterns = [
    path("publicaciones/", views.publicaciones, name="publicaciones"),
    path("publicacion/<int:pk>/", views.detalle_publicacion, name="detalle_publicacion"),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('administradores/', views.administradores, name='administradores'),
]
