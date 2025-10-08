from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistroForm

def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro exitoso. ¡Ya puedes iniciar sesión!")
            return redirect("home:home")
    else:
        form = RegistroForm()
    return render(request, "cuentas/registro.html", {"form": form})
