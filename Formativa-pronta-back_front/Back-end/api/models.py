from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    ESCOLHA= [
        ('P', 'Professor'),
        ('G',  'Gestor')
    ]
    categoria= models.CharField(max_length=1, choices=ESCOLHA, default='G')
    ni= models.IntegerField(unique=True)
    telefone= models.CharField(max_length=10)
    data_nascimento= models.DateField(blank=True, null=True)
    data_contracao= models.DateField(blank=True, null=True)
    REQUIRED_FIELDS=['ni', 'categoria', 'telefone']

    def __str__(self):
        return f'{self.username} ({self.get_categoria_display()})'


class Disciplina(models.Model):
    nome= models.CharField(max_length=15)
    curso= models.CharField(max_length=30)
    carga_horaria= models.IntegerField()
    descricao= models.TextField()
    professor_responsavel = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="disciplinas", limit_choices_to={'categoria': 'P'})
    
    def __str__(self):
        return self.nome

class ReservaAmbiente(models.Model):
    data_inicio= models.DateField()
    data_termino= models.DateField()
    periodo= models.CharField(max_length=20)
    sala= models.CharField(max_length=20)
    professor_responsavel= models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="reservas")
    disciplina= models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name="reservas")

    def __str__(self):
        return f"{self.sala} - {self.periodo} ({self.data_inicio} a {self.data_termino})"