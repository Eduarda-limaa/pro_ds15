from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .serializers import UsuarioSerializer

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
        return Response({"Erro": "Digite o usuário e senha correta!!"}, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_protegida(request):
    return Response({"Mensagem": "O seu cadastro realmente está seguro!"}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listar_usuarios(rquest):
    usuarios= Usuario.objects.all()
    serializer= UsuarioSerializer(usuarios, many= True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listar_usuario(request, pk):
    try:
        usuario= Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return Response({'Erro': 'Este usuário não existe'}, status=status.HTTP_404_NOT_FOUND)

    serializer= UsuarioSerializer(usuario)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_usuario(request, pk):
    from django.contrib.auth.hashers import make_password
    try:
        usuario= Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    request.data['password']= make_password(request.data['password'])
   
    serializer= UsuarioSerializer(usuario, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_usuario(request, pk):
    try:
        usuario= Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    usuario.delete()
    return Response({"Mensagem": "Usuario deletado com sucesso!"}, status=status.HTTP_204_NO_CONTENT)