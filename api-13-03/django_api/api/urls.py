from django.urls import path
from . import views

urlpatterns= [
    path('api/', views.read_pokemons, name='read_pokemons'),
    path('api/<int:pk>', views.read_pokemon), 
    path('api/criar/', views.create_pokemon, name='create_pokemon'),
    path('api/atualizar/<int:pk>', views.update_pokemon, name='update_pokemon'),
    path('api/deletar/<int:pk>', views.delete_pokemon, name='delete_pokemon'),
    path('api/atualizarPartes/<int:pk>', views.update_parcial_pokemon)
]
