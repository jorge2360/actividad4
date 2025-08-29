from django.shortcuts import render

# Create your views here.
def estudiantes(request):
    return render(request, 'estudiantes/estudiantes.html')