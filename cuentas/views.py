from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistroForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro exitoso. ¡Ya puedes iniciar sesión!")
            return redirect("cuentas:login")
    else:
        form = RegistroForm()
    return render(request, "cuentas/registro.html", {"form": form})

def login_usuario(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Bienvenido, {user.username}")
            return redirect("home:home")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    return render(request, "cuentas/login.html")


def logout_usuario(request):
    logout(request)
    messages.info(request, "Sesión cerrada correctamente.")
    return redirect("cuentas:login")