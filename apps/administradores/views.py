from django.shortcuts import render

# Create your views here.
def administradores(request):
    return render(request, 'administradores/administradores.html')