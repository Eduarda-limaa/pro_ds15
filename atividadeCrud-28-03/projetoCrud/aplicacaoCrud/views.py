from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario

@api_view(['POST'])
def registrar(request):
    nome= request.data.get('username')
    senha= request.data.get('senha')
    telefone= request.data.get('telefone')
    idade= request.data.get('idade')
    biografia= request.data.get('biografia')
    endereco= request.data.get('endereco')
    escolaridade= request.data.get('escolaridade')
    animais= request.data.get('animais')

    if not nome or not senha or not idade:
        return Response({'Erro': 'Os campos, nome, senha, idade são obrigatorios'}, status=status.HTTP_400_BAD_REQUEST)
    
    if Usuario.objects.filter(username=nome).exists():
        return Response({'Erro': 'Esse username está sendo usado, coloque outro.'}, status=status.HTTP_400_BAD_REQUEST)

    usuario= Usuario.objects.create_user(
        username= nome,
        password= senha,
        telefone= telefone,
        idade= idade,
        biografia= biografia,
        endereco= endereco,
        escolaridade= escolaridade,
        animais= animais
    )

    return Response({'Mensagem': 'Usuario cadastrado com sucesso1'}, status=status.HTTP_201_CREATED)
    

