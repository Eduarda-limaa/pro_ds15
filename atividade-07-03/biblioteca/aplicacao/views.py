from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from .forms import Bibliotecaform

def crud_read(request):
    biblioteca = Livro.objects.all()
    return render(request, 'crud_read.html', {'listas': biblioteca})


def crud_create(request):
    if request.method== 'POST':
        form = Bibliotecaform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud_read')
        
    else:
        form= Bibliotecaform()
    return render(request, 'crud_form.html', {'form': form})

def crud_update(request, pk):
    biblioteca = get_object_or_404(Livro, pk=pk)
    if request.method == 'post':
        form= Bibliotecaform(request.POST, instance=biblioteca)
        if form.is_valid():
            form.save()
            return redirect('crud_read')
    else:
        form= Bibliotecaform(instance= biblioteca)
    return render(request, 'crud_form.html', {'form':form})

def crud_delete(request, pk):
    biblioteca= get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        biblioteca.delete()
        return redirect('crud_read')
    return render(request, 'confirmacao_delete.html', {'biblioteca': biblioteca})

def buscar_livros(request):
    titulos= request.GET.get('titulo', '')
    autor= request.GET.get('autor', '')
    ano= request.GET.get('ano', '')

    livros= Livro.objects.all()

    if titulos: 
        livros= livros.filter(titulos__icontains=titulos)

    if autor:
        livros= livros.filter(autor__icontains=autor)

    if ano:
        livros= livros.filter(ano=ano)
    
    return render(request, 'lista_livros.html', {'livros': livros})