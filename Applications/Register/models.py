from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.contrib.auth.hashers import make_password, check_password

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
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class Users(AbstractBaseUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Asegúrate de que este campo no sea necesario si heredamos de AbstractBaseUser
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)  # Este campo es parte del modelo AbstractBaseUser

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def set_password(self, raw_password):
        """Establece la contraseña de manera segura usando el hash adecuado."""
        self.password = make_password(raw_password)  # Usamos make_password para generar el hash
        self.save()

    def check_password(self, raw_password):
        """Verifica si la contraseña proporcionada coincide con el hash almacenado."""
        return check_password(raw_password, self.password)  # Verificamos el hash






