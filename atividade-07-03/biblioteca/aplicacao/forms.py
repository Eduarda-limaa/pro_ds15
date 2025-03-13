from django import forms
from .models import Livro

class Bibliotecaform(forms.ModelForm):
    class Meta:
        model= Livro
        fields= ['titulos', 'autor', 'ano', 'editora']