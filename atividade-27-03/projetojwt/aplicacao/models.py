from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    telefone= models.CharField(max_length=15, null=True, blank=True)
    cpf= models.CharField(max_length=20, null=True, blank=True)
    endereco= models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username