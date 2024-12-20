from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class PagoForm(forms.Form):
    numero_tarjeta = forms.CharField(
        label="Número de la tarjeta",
        max_length=19,  # Máximo incluyendo espacios (#### #### #### ####)
        widget=forms.TextInput(attrs={
            'placeholder': '1234 1234 1234 1234',
            'class': 'form-control'
            })
    )
    fecha_caducidad = forms.CharField(
        label="Fecha de Caducidad",
        max_length=7,  # Máximo 7 caracteres para "MM/AAAA"
        widget=forms.TextInput(attrs={
            'placeholder': 'MM/AAAA',
            'class': 'form-control',
            'inputmode': 'numeric',
        })
    )
    cvv = forms.IntegerField(
        label="Código de seguridad",
        validators=[
            MaxValueValidator(999),  # Máximo número de 3 dígitos
            MinValueValidator(100), # Mínimo número de 3 dígitos
        ],
        widget=forms.PasswordInput(attrs={
            'placeholder': '123',
            'class': 'form-control',
            'maxlength': '3',  # Limita a 3 caracteres en el frontend
            'inputmode': 'numeric',  # Teclado numérico en dispositivos móviles
        })
    )
    
    nombre_titular = forms.CharField(
        label="Titular de la Tarjeta",
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Nombre del titular',
            'class': 'form-control'
            })
    )
    email = forms.EmailField(
        label="Correo Electrónico",
        widget=forms.EmailInput(attrs={
            'placeholder': 'Correo Electrónico',
            'class': 'form-control'
            })
    )
    confirmar_email = forms.EmailField(
        label="Repetir Correo Electrónico",
        widget=forms.EmailInput(attrs={
            'placeholder': 'Confirmar Correo Electrónico',
            'class': 'form-control'
            })
    )
    dni = forms.IntegerField(
        label="DNI",
        validators=[MaxValueValidator(99999999)],
        widget=forms.TextInput(attrs={
            'placeholder': 'Número de DNI',
            'class': 'form-control'
            })
    )

    # Validación adicional para confirmar que los emails coincidan
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        confirmar_email = cleaned_data.get("confirmar_email")

        if email != confirmar_email:
            self.add_error('confirmar_email', "Los correos electrónicos no coinciden.")
