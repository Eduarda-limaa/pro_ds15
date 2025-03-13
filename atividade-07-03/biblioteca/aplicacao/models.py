from django.db import models

class Livro(models.Model):
    titulos= models.CharField(max_length=20)
    autor= models.CharField(max_length=30)
    ano= models.IntegerField()
    editora= models.CharField(max_length=20)
    

    def __str__(self):
        return f"O titulo do livro é: {self.titulos}, o nome do autor é: {self.autor}. O ano de publicação do livro é: {self.ano} e a editora é: {self.editora}"

# Create your models here.
