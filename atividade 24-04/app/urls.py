from django.urls import path
from .views import *

urlpatterns = [
    path('login/', view=LoginView.as_view()),
    path('produto/', view=ProdutoListCreateAPIView.as_view()),
    path('usuario/<int:pk>/', view=UsuarioRetrieveUpdateDestroyAPIView.as_view()),
    path('usuario/', view=UsuarioListCreateAPIView.as_view),
]