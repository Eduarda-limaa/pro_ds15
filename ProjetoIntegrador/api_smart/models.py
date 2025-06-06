from django.db import models
from django.contrib.auth.models import AbstractUser

class Sensores(models.Model):
    sensor= models.CharField(max_length=15)
    mac_address= models.CharField(max_length=20)
    unidade_med= models.CharField(max_length=20)
    latitude= models.FloatField()
    longitude= models.FloatField()
    status= models.BooleanField()

    def __str__(self):
        return f"O status está {self.status} e o sensor é {self.sensor}"

class Ambientes(models.Model):
    sig= models.IntegerField()
    descricao= models.TextField()
    ni= models.CharField(max_length=20)
    responsavel= models.CharField(max_length=50)

    def __str__(self):
        return f"O responsavel do ambiente é {self.responsavel} e o ni é {self.ni}"


class Historico(models.Model):
    sensor= models.ForeignKey(Sensores, on_delete=models.CASCADE, related_name="historico")
    ambiente= models.ForeignKey(Ambientes, on_delete=models.CASCADE, related_name="historico")
    valor= models.FloatField()
    timestamp= models.DateTimeField()

    def __str__(self):
        return f"{self.ambiente} - {self.sensor} - {self.valor} - {self.timestamp}"


