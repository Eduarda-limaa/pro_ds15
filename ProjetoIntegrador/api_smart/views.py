from django.shortcuts import render
from .serializers import SensoresSerializer, AmbientesSerializer, HistoricoSerializer
from .models import Sensores, Ambientes, Historico
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView 
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse
import pandas as pd
from rest_framework.views import APIView


#Lista e criação de sensores. Permite filtragem por unidade de medida
class ListCreateSensores(ListCreateAPIView):
    permission_classes= [IsAuthenticated]
    serializer_class= SensoresSerializer
    queryset= Sensores.objects.all()
    filter_backends= [DjangoFilterBackend]
    filterset_fields= ['unidade_med']


#Consulta, atualização e delete para dados des sensores específico
class RetrieveUpdateDestroySensores(RetrieveUpdateDestroyAPIView):
    permission_classes= [IsAuthenticated]
    serializer_class= SensoresSerializer
    queryset= Sensores.objects.all()


#Lista e criação de Ambientes. Permite filtragem pelo "sig"
class ListCreateAmbientes(ListCreateAPIView):
    permission_classes= [IsAuthenticated]
    serializer_class= AmbientesSerializer
    queryset= Ambientes.objects.all()
    filter_backends= [DjangoFilterBackend]
    filterset_fields= ['sig']


#Consulta, atualização e delete para dados dos ambientes específicos
class RetrieveUpdateDestroyAmbientes(RetrieveUpdateDestroyAPIView):
    permission_classes= [IsAuthenticated]
    serializer_class= AmbientesSerializer
    queryset= Ambientes.objects.all()

#Lista e criação de Historico.
#Filtro para selecionar dados especificos como sensor, timestamp e id
class ListCreateHistorico(ListCreateAPIView):
    permission_classes= [IsAuthenticated]
    serializer_class= HistoricoSerializer
    queryset= Historico.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sensor', 'timestamp', 'id']

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

#Consulta, atualização e delete para dados dos historicos específicos
class RetrieveUpdateDestroyHistorico(RetrieveUpdateDestroyAPIView):
    permission_classes= [IsAuthenticated]
    serializer_class= HistoricoSerializer
    queryset= Historico.objects.all()

    
# Exporta um arquivo excel dos dados do Sensor
class ExportarSensor(APIView):
    permission_classes= [IsAuthenticated]
    def get(self, request): 
        sensor= Sensores.objects.all()

        dados= []
        for i in sensor:
            dados.append({
                'Sensor': i.sensor,
                'mac_address': i.mac_address,
                'unidade_med': i.unidade_med,
                'latitude': i.latitude,
                'longitude': i.longitude,
                'status': i.status
            })
        df= pd.DataFrame(dados)

        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename="sensores.xlsx"'

        with pd.ExcelWriter(response, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Sensores')

        return response



# Exporta um arquivo excel dos dados do Ambiente
class ExportarAmbiente(APIView):
    permission_classes= [IsAuthenticated]
    def get(self, request): 
        ambientes= Ambientes.objects.all()

        dados= []
        for i in ambientes:
            dados.append({
                'Sig': i.sig,
                'Descrição': i.descricao,
                'NI': i.ni,
                'Resposavel': i.responsavel,
            })
        df= pd.DataFrame(dados)

        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename="ambientes.xlsx"'

        with pd.ExcelWriter(response, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Ambientes')

        return response
    

# Exporta um arquivo excel dos dados do Historico
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
                'Data e hora': str(i.timestamp), 
            })
        df= pd.DataFrame(dados)

        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename="historico.xlsx"'

        with pd.ExcelWriter(response, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Histórico')

        return response
