from django.db import models
from django.core.validators import RegexValidator


class BichoEstimacao(models.Model):
    nome= models.CharField(max_length=20)
    opcoes_racas= (
        ('Coruja', 'Coruja'),
        ('Gato', 'Gato'),
        ('Rato', 'Rato'),
        ('Cobra', 'Cobra')
    )
    raca= models.CharField(max_length=20, choices=opcoes_racas)

    def __str__(self):
        return self.nome

class PersonagemHarryPotter(models.Model):
    nome = models.CharField(max_length=50)
    escolha_casas =(
        ('GRI', 'Grifinoria'),
        ('SON', 'Sonserina'),
        ('LUF', 'Lufa-Lufa'),
        ('COR', 'Corvinal')
    )
    casa= models.CharField(max_length=25, choices=escolha_casas)
    validador_cpf= RegexValidator(
        regex='^\d{3}.\d{3}.\d{3}-\d{2}$',
        message='O CPF do bruxo deve ser no formato xxx.xxx.xxx-xx'
    )
    CPF = models.CharField(max_length=14, validators=[validador_cpf], unique=True)
    qnt_de_nariz= models.IntegerField(blank=True, null=True)
    status= models.BooleanField()
    patrono= models.CharField(max_length=255, blank=True, null=True)
    animal= models.ForeignKey(BichoEstimacao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome



