from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'administradores'
urlpatterns = [
    path('', views.administradores, name="administradores"),
]
