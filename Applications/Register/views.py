from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UsersCreationForm
from .models import Users, CustomUser
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth.hashers import check_password 
from django.contrib.auth.decorators import login_required


def register_view(request):
    if request.method == 'POST':
        form = UsersCreationForm(request.POST)  # Asegúrate de usar UsersCreationForm aquí
        if form.is_valid():
            user = form.save(commit=False)  # No guardamos el usuario aún
            user.set_password(form.cleaned_data['password1'])  # Llamamos a set_password
            user.save()  # Guardamos el usuario
            messages.success(request, 'Cuenta creada exitosamente. Inicie sesión.')
            return redirect("register:login")
    else:
        form = UsersCreationForm()  # Y aquí también
    return render(request, 'register/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Intentar autenticar al usuario en CustomUser
            try:
                # Primero, buscamos el usuario en CustomUser
                user = CustomUser.objects.get(email=email)
                if user.check_password(password):  # Verificamos la contraseña
                    login(request, user)  # Iniciamos sesión
                    return redirect('movie:index')  # Redirigir al índice
                else:
                    messages.error(request, 'Contraseña incorrecta.')
            except CustomUser.DoesNotExist:
                # Si no encontramos el usuario en CustomUser, buscamos en Users
                try:
                    user = Users.objects.get(email=email)
                    if user.check_password(password):  # Verificamos la contraseña
                        # Iniciamos sesión manualmente
                        login(request, user)  # Aunque 'Users' no tiene autenticación nativa
                        return redirect('movie:index')  # Redirigir al índice
                    else:
                        messages.error(request, 'Contraseña incorrecta.')
                except Users.DoesNotExist:
                    messages.error(request, 'No se encontró un usuario con ese correo.')
            
    else:
        form = LoginForm()  # Si no es POST, mostramos el formulario vacío

    return render(request, 'register/login.html', {'form': form})

@login_required
def profile_view(request):
    return render(request, 'register/profile.html')

















