from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email debe ser proporcionado')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Encriptamos la contraseña
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('El superusuario debe tener is_staff=True.')
        if not extra_fields.get('is_superuser'):
            raise ValueError('El superusuario debe tener is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name='Correo Electrónico')
    is_active = models.BooleanField(default=True, verbose_name='Activo')  # Para habilitar/deshabilitar usuarios
    is_staff = models.BooleanField(default=False, verbose_name='Es Staff')  # Define si el usuario puede acceder al admin
    is_superuser = models.BooleanField(default=False, verbose_name='Es Superusuario')  # Define si es superusuario

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  # Campo usado como identificador
    REQUIRED_FIELDS = []  # Sin campos adicionales requeridos

    def __str__(self):
        return self.email
