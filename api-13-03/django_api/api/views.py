from django.shortcuts import render
from .models import Pokemon
from rest_framework.response import Response
from .serializers import PokemonSerializer
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET'])
def read_pokemons(request):
    pokemons= Pokemon.objects.all()
    serializer = PokemonSerializer(pokemons, many= True)
    return Response(serializer.data)

@api_view(['GET'])
def read_pokemon(request, pk):
    try:
        pokemon= Pokemon.objects.get(pk=pk)
    except Pokemon.DoesNotExist:
        return Response({'Erro': 'Este pokemon não existe'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer= PokemonSerializer(pokemon)
    return Response(serializer.data)

@api_view(['POST'])
def create_pokemon(request):
    if request.method == 'POST':
        serializer= PokemonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def update_pokemon(request, pk):
    try:
        pokemon= Pokemon.objects.get(pk=pk)
    except Pokemon.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer= PokemonSerializer(pokemon, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_pokemon(request, pk):
    try:
        pokemon= Pokemon.objects.get(pk=pk)
    except Pokemon.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    pokemon.delete()
    return Response({"Mensagem": "Pokemon apagado com sucesso!"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['PATCH'])
def update_parcial_pokemon(request, pk):
    try:
        pokemon= Pokemon.objects.get(pk=pk)
    except Pokemon.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer= PokemonSerializer(pokemon, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)