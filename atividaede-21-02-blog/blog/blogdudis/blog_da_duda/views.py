from django.shortcuts import render
from .models import Postagem

def listar_postagem(request):
    postagens= Postagem.objects.all().order_by('--decricao')
    return render(request, 'blog/lista_postagem.html', {'postagem': postagens})

# Create your views here.
