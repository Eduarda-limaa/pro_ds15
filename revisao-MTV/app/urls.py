from .views import *
from django.urls import path

urlpatterns = [
    path('listar/', view=listar_personagens, name='listar_personagens'),
    path('criar/', view=criar_bruxo, name='criar_bruxo'),
    path('atualizar/<int:pk>/', view=atualizar_bruxo, name='atualizar_bruxo'),
    path('deletar/<int:pk>/', view=deletar_bruxo, name='deletar_bruxo')
]