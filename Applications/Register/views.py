from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth.decorators import login_required

def register_view(request):
    """
    Vista para registrar un nuevo usuario común.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])  # Establecer contraseña segura
            user.is_staff = False  # Asegurar que no sea staff
            user.is_superuser = False  # Asegurar que no sea superusuario
            user.save()
            messages.success(request, 'Cuenta creada exitosamente. Ahora puedes iniciar sesión.')
            return redirect("register:login")  # Redirige al login
        else:
            messages.error(request, 'Por favor, corrige los errores del formulario.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register/register.html', {'form': form})


def login_view(request):
    """
    Vista para iniciar sesión en la aplicación.
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, email=email, password=password)  # Autentica contra CustomUser
            if user is not None:
                if user.is_active:  # Verifica si la cuenta está activa
                    login(request, user)  # Inicia sesión
                    messages.success(request, f"Bienvenido, {user.email}!")
                    return redirect('movie:index')  # Redirige a la página principal
                else:
                    messages.error(request, 'Tu cuenta está desactivada. Contacta al administrador.')
            else:
                messages.error(request, 'Correo o contraseña incorrectos. Intenta nuevamente.')
    else:
        form = LoginForm()

    return render(request, 'register/login.html', {'form': form})


@login_required
def profile_view(request):
    """
    Vista para mostrar el perfil del usuario logueado.
    """
    return render(request, 'register/profile.html')
