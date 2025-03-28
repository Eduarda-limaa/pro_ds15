from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario
from django.contrib.auth import authenticate 
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
def registrar(request):
    nome= request.data.get('username')
    senha= request.data.get('senha')
    telefone= request.data.get('telefone')
    endereco= request.data.get('endereco')
    cpf= request.data.get('cpf')
    email= request.data.get('email')

    if not nome or not senha or not cpf or not email:
        return Response({'Erro': 'Os campos, nome, senha, cpf e email são obrigatorios'}, status=status.HTTP_400_BAD_REQUEST)
    
    if Usuario.objects.filter(username=nome).exists():
        return Response({'Erro': 'Esse username está sendo usado, coloque outro.'}, status=status.HTTP_400_BAD_REQUEST)

    usuario= Usuario.objects.create_user(
        username= nome,
        password= senha,
        telefone= telefone,
        email= email,
        cpf= cpf,
        endereco= endereco 
    )

    return Response({'Mensagem': 'Usuario cadastrado com sucesso1'}, status=status.HTTP_201_CREATED)
    

@api_view(['POST'])
def logar(request):
    nome= request.data.get('username')
    senha= request.data.get('senha')

    user= authenticate(username= nome, password= senha)

    if user:
        refresh= RefreshToken.for_user(user)
        return Response({
            'acesso': str(refresh.access_token),
            'refresh': str(refresh),
        }, status=status.HTTP_200_OK)
    else:
        return Response({"Erro": "Digite o usuario e senha correta!!"}, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['GET'])
@permission_classes({IsAuthenticated})
def view_protegida(request):
    return Response({"Mensagem": "Olá ds15"}, status=status.HTTP_200_OK)