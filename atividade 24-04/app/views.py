# from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import LoginSerializer, UsuarioSerializer, ProdutoSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Usuario, Produto
from .permissions import *
from rest_framework import permissions

class LoginView(TokenObtainPairView):
    serializer_class= LoginSerializer

class UsuarioListCreateAPIView(ListCreateAPIView):
    queryset= Usuario.objects.all()
    serializer_class= UsuarioSerializer
    permission_classes = [IsGestor]

class UsuarioRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset= Usuario.objects.all()
    serializer_class= UsuarioSerializer
    permission_classes = [IsGestor]
    lookup_field= 'pk'

class ProdutoListCreateAPIView(ListCreateAPIView):
    queryset= Produto.objects.all()
    serializer_class= ProdutoSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAuthenticated()]
        return [IsFuncionario()]