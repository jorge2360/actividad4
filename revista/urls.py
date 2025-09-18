from django.urls import path
from . import views
app_name = 'publicaciones'
urlpatterns = [
    path("", views.lista_publicaciones, name="lista_publicaciones"),
    path("publicacion/<int:pk>/", views.detalle_publicacion, name="detalle_publicacion"),
    path("crear/", views.crear_publicacion, name="crear_publicacion"),
]