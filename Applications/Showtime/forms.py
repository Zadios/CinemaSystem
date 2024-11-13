from django import forms

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
        max_length=7,  # Para formato "MM/AAAA"
        widget=forms.TextInput(attrs={
            'placeholder': 'MM/AAAA',
            'class': 'form-control'
            })
    )
    cvv = forms.CharField(
        label="Código de seguridad",
        max_length=4,  # Permitir 3 o 4 dígitos
        widget=forms.PasswordInput(attrs={
            'placeholder': '123',
            'class': 'form-control'
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
    dni = forms.CharField(
        label="DNI",
        max_length=10,
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
