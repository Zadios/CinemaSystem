from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UsersCreationForm, CustomAuthenticationForm  # Asegúrate de que CustomAuthenticationForm esté aquí
from .models import Users

def register_view(request):
    if request.method == 'POST':
        form = UsersCreationForm(request.POST)  # Asegúrate de usar UsersCreationForm aquí
        if form.is_valid():
            user = form.save()  # Guardar usuario
            messages.success(request, 'Cuenta creada exitosamente. Inicie sesión.')
            return redirect("login-register:login")
    else:
        form = UsersCreationForm()  # Y aquí también
    return render(request, 'register/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)  # Autenticación con correo
            if user is not None:
                login(request, user)
                return redirect('pelicula-list')  # Cambia esto por tu vista deseada
            else:
                messages.error(request, 'Email o contraseña incorrectos.')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'register/login.html', {'form': form})















