from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    biografia= models.TextField(blank=True, null=True)
    idade= models.IntegerField()
    telefone= models.CharField(max_length= 15, blank=True, null=True)
    endereco= models.CharField(max_length= 255, blank=True, null=True)
    escolaridade= models.CharField(max_length= 20, blank=True, null=True)
    animais= models.CharField(max_length= 20, blank=True, null=True)
    REQUIRED_FIELDS = ['idade']

    def __str__(self):
        return self.username