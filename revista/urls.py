from django.urls import path
from . import views
app_name = 'revista'
urlpatterns = [
    path("publicaciones/", views.publicaciones, name="publicaciones"),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('administradores/', views.administradores, name='administradores'),
    # Estudiantes
    path("estudiantes/<int:pk>/", views.EstudianteDetailView.as_view(), name="estudiante_detail"),
    path("estudiantes/<int:pk>/editar/", views.EstudianteUpdateView.as_view(), name="estudiante_edit"),

    # Administradores
    path("administradores/<int:pk>/", views.AdministradorDetailView.as_view(), name="administrador_detail"),
    path("administradores/<int:pk>/editar/", views.AdministradorUpdateView.as_view(), name="administrador_edit"),

    # Publicaciones
    path("publicaciones/<int:pk>/", views.PublicacionDetailView.as_view(), name="publicacion_detail"),
    path("publicaciones/<int:pk>/editar/", views.PublicacionUpdateView.as_view(), name="publicacion_edit"),
]
