from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'estudiantes'
urlpatterns = [
    path('', views.estudiantes, name="estudiantes"),
]
