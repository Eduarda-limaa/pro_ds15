from django.db import models

class Evento(models.Model):
    nome= models.CharField(max_length=20)
    descriacao= models.TextField()
    data_hora= models.DateTimeField()
    local= models.CharField(max_length=40, blank=True)
    categoria= models.TextField(blank=True)

    def __str__(self):
        return self.nome