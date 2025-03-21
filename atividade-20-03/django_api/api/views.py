from django.shortcuts import render
from .models import Evento
from rest_framework.response import Response
from .serializers import EventoSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from django.utils import timezone
from datetime import timedelta

@api_view(['GET'])
def read_eventos(request):
    eventos = Evento.objects.all()
    categoria = request.query_params.get('categoria', None)
    if categoria:
        eventos = eventos.filter(categoria__icontains=categoria)

    data_inicio = request.query_params.get('data_inicio', None)
    if data_inicio: 
        eventos = eventos.filter(data_hora__gte=data_inicio)

    data_fim = request.query_params.get('data_fim', None)
    if data_fim:
        eventos = eventos.filter(data_hora__lte=data_fim)

    quantidade_min = request.query_params.get('quantidade_min', None)
    if quantidade_min:
        eventos = eventos.filter(quantidade__gte=quantidade_min)

    quantidade_max = request.query_params.get('quantidade_max', None)
    if quantidade_max:
        eventos = eventos.filter(quantidade__lte=quantidade_max)

    ordenar_por_data = request.query_params.get('ordenar_por_data', None)
    if ordenar_por_data:
        eventos = eventos.order_by(ordenar_por_data)
        # if ordenar_por_data == 'data':
           
        # elif ordenar_por_data == '-data':
        #     eventos = eventos.order_by('-data_hora')
        
    serializer = EventoSerializer(eventos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def read_evento(request, pk):
    try:
        evento= Evento.objects.get(pk=pk)
    except Evento.DoesNotExist:
        return Response({'Erro': 'Este evento não existe'}, status=status.HTTP_404_NOT_FOUND)
    serializer= EventoSerializer(evento)
    return Response(serializer.data)

@api_view(['GET'])
def read_eventosproximos(request):
    data_hoje= timezone.now()
    sete_dias= data_hoje + timedelta(days=7)
    eventos_proximos= Evento.objects.filter(data_hora__gte=data_hoje, data_hora__lte=sete_dias)

    serializer= EventoSerializer(eventos_proximos, many= True)
    return Response(serializer.data)

@api_view(['POST'])
def create_evento(request):
    if request.method == 'POST':
        serializer= EventoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_evento(request, pk):
    try:
        evento = Evento.objects.get(pk=pk)
    except Evento.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

   
    serializer= EventoSerializer(evento, data= request.data)
    if serializer.is_valid():
       serializer.save()
       return Response(serializer.data, status=status.HTTP_200_OK) 
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

@api_view(['DELETE'])
def delete_evento(request, pk):
    try:
        evento= Evento.objects.get(pk=pk)
    except Evento.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    evento.delete()
    return Response({"Mensagem": "Pokemon apagado com sucesso!"})
    status=status.HTTP_204_NO_CONTENT