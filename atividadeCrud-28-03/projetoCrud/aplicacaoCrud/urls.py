from django.urls import path
from . import views

urlpatterns=[
    path('criar/', view=views.registrar, name='registrar'),
    path('logar/', view=views.logar, name='logar'),
    path('protegido/', view=views.view_protegida, name='view protegida'),
    path('listar/', view=views.listar_usuarios, name='Listar todos os usuarios'),
    path('listar/<int:pk>', view=views.listar_usuario, name='Lista o usuário pelo id'),
    path('atualizar/<int:pk>', view=views.update_usuario, name='atualizar o usuario'),
    path('deletar/<int:pk>', view=views.delete_usuario, name='deletar o usuário'),
]