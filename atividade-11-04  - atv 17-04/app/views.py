from django.shortcuts import render
from .models import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import *
from rest_framework.pagination import PageNumberPagination
import re
from rest_framework_simplejwt.views import TokenObtainPairView

class AniversariantePaginacao(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 20

class AniversarianteListCreateAPIView(ListCreateAPIView):
    queryset = Aniversariante.objects.all()
    serializer_class = AniversarianteSerializer
    pagination_class = AniversariantePaginacao
    
    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.query_params.get('nome')
        if nome:
            queryset = queryset.filter(nome__icontains = nome)
        return queryset
    
    def perform_create(self, serializer):
        cpf = serializer.validated_data['cpf']
        data = serializer.validated_data['data']
        idade = serializer.validated_data['idade']
        if not re.match(r'^\d{3}.\d{3}.\d{3}-\d{2}$', cpf):
            raise serializers.ValidationError("CPF deve ser no formato adequado")
        if 2025-data.year != idade:
            raise serializers.ValidationError("A idade não compactua com a data")
        serializer.save()

class AniversarianteRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset= Aniversariante.objects.all()
    serializer_class= AniversarianteSerializer
    lookup_field= 'pk'

class LoginView(TokenObtainPairView):
    serializer_class= LoginSerializer