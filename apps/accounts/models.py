from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from .managers import CustomUserManager


class User(AbstractUser):
    phone = models.CharField(max_length=25, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    state = models.CharField(max_length=150, blank=True, null=True)
    country = models.CharField(max_length=150, blank=True, null=True)
    
    username = None
    email = models.EmailField(("email address"), unique=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


    # Agregar el argumento related_name para evitar el conflicto
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_accounts'
    )

    # Agregar el argumento related_name para evitar el conflicto
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_accounts'
    )

    objects = CustomUserManager()

    def __str__(self):
        return self.email
