from django.shortcuts import render, redirect
from .models import User
from .encriptacion import validatePassword, cryptPassword
from .forms import LoginForm, RegisterForm

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            try:
                user = User.objects.get(email=email)
                if validatePassword(password, user.password):
                    return render(request, "dashboard.html", {"user": user})
                else:
                    return render(request, "error.html", {"mensaje": "Contraseña incorrecta"})
            except User.DoesNotExist:
                return render(request, "error.html", {"mensaje": "Usuario no encontrado"})
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            role = form.cleaned_data["role"]

            encrypted_password = cryptPassword(password)
            User.objects.create(email=email, password=encrypted_password, role=role)
            return redirect("login")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})


def dashboard_view(request):
    return render(request, "dashboard.html", {"user": request.user})

