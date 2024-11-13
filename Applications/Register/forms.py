from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Users
from django.contrib.auth.forms import AuthenticationForm  # Importación correcta


class UsersCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'placeholder': 'Ingresa una contraseña'}),
        min_length=8
    )
    password2 = forms.CharField(
        label='Confirmar Contraseña',
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirma la contraseña'}),
        min_length=8
    )

    class Meta:
        model = Users
        fields = ['email']  # Solo estamos incluyendo el campo email, asegúrate de que esté aquí

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Users.objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe un usuario registrado con ese correo.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data


class CustomAuthenticationForm(AuthenticationForm):
    """Formulario de autenticación personalizado."""
    
    username = forms.EmailField(label='Email', max_length=254)

    def clean(self):
        """Verifica las credenciales del usuario."""
        super().clean()
        # Puedes agregar validaciones adicionales aquí si lo deseas







