from django.shortcuts import render
from .serializers import SensoresSerializer, AmbientesSerializer, HistoricoSerializer
from .models import Sensores, Ambientes, Historico
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters import DjangoFilterBackend


#lista e criação de sensores
class ListCreateSensores(ListCreateAPIView):
    permission_classes= [IsAuthenticated]
    serializer_class= SensoresSerializer
    queryset= Sensores.objects.all()


#consulta, atualização e delete para dados dos sensores
class RetrieveUpdateDestroySensores(RetrieveUpdateDestroyAPIView):
    permission_classes= [IsAuthenticated]
    serializer_class= SensoresSerializer
    queryset= Sensores.objects.all()


#lista e criação de Ambientes
class ListCreateAmbientes(ListCreateAPIView):
    permission_classes= [IsAuthenticated]
    serializer_class= AmbientesSerializer
    queryset= Ambientes.objects.all()


#consulta, atualização e delete para dados dos ambientes
class RetrieveUpdateDestroyAmbientes(RetrieveUpdateDestroyAPIView):
    permission_classes= [IsAuthenticated]
    serializer_class= AmbientesSerializer
    queryset= Ambientes.objects.all()

#lista e criação de Historico
class ListCreateHistorico(ListCreateAPIView):
    permission_classes= [IsAuthenticated]
    serializer_class= HistoricoSerializer
    queryset= Historico.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sensor', 'ambiente', 'timestamp']

#consulta, atualização e delete para dados dos historicos
class RetrieveUpdateDestroyHistorico(RetrieveUpdateDestroyAPIView):
    permission_classes= [IsAuthenticated]
    serializer_class= HistoricoSerializer
    queryset= Historico.objects.all()