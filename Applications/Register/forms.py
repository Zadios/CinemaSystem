from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser


class CustomUserCreationForm(forms.ModelForm):
    email = forms.CharField(
        label='Correo electrónico',
        widget=forms.EmailInput(attrs={'placeholder': 'Ingresar correo'}),
    )
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
        model = CustomUser
        fields = ['email']  # Solo estamos incluyendo el campo email

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe un usuario registrado con ese correo.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])  # Establece la contraseña de manera segura
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.EmailField(
        label='Correo electrónico', 
        max_length=254, 
        widget=forms.EmailInput(attrs={'placeholder': 'Ingresar correo', 'class': 'custom-input'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Ingresar contraseña', 'class': 'custom-input'}),
        label="Contraseña"
    )
