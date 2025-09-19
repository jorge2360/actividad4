from django.urls import path
from . import views
app_name = 'revista'
urlpatterns = [
    path("publicaciones/", views.publicaciones, name="publicaciones"),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('administradores/', views.administradores, name='administradores'),
    path('agregar-publicador/', views.agregar_publicador, name='agregar_publicador'),
    path('agregar-autorizador/', views.agregar_autorizador, name='agregar_autorizador'),
    path('agregar-publicacion/', views.agregar_publicacion, name='agregar_publicacion'),

]
