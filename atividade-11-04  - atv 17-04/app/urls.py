from . import views
from django.urls import path

urlpatterns = [
    path('aniversariante/', view=views.AniversarianteListCreateAPIView.as_view(), name='listar_criar_aniversariante'),
    path('aniversariante/<int:pk>', view=views.AniversarianteRetrieveUpdateDestroy.as_view(), name='atualizar_deletar_visualizar'),
    path('logar/', view=views.LoginView.as_view(), name='login'),
]