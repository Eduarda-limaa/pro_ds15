from django.shortcuts import render
from .serializers import SensoresSerializer, AmbientesSerializer, HistoricoSerializer
from .models import Sensores, Ambientes, Historico
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView 
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse
from pandas import pd
from rest_framework.views import APIView


#lista e criação de sensores
class ListCreateSensores(ListCreateAPIView):
    permission_classes= [IsAuthenticated]
    serializer_class= SensoresSerializer
    queryset= Sensores.objects.all()
    filter_backends= [DjangoFilterBackend]
    filterset_fields= ['unidade_med']


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
    filter_backends= [DjangoFilterBackend]
    filterset_fields= ['sig']


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
    filterset_fields = ['sensor', 'timestamp', 'id']

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

#consulta, atualização e delete para dados dos historicos
class RetrieveUpdateDestroyHistorico(RetrieveUpdateDestroyAPIView):
    permission_classes= [IsAuthenticated]
    serializer_class= HistoricoSerializer
    queryset= Historico.objects.all()


#funcao que exporta os dados de historico para 
class ExportarHistorico(APIView):
    permission_classes= [IsAuthenticated]

    def get(self, request): 
        historicos= Historico.objects.select_related('sensor', 'ambiente').all()

        dados= []
        for i in historicos:
            dados.append({
                'ID': i.id,
                'Sensor': i.sensor.sensor,
                'Mac Address': i.sensor.mac_address,
                'Ambiente (sig)': i.ambiente.sig,
                'Valor': i.valor,
                'Data e hora': i.timestamp, 
            })


        df= pd.DataFrame(dados)

        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename="historico.xlsx"'

        with pd.ExcelWriter(response, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Histórico')

        return response