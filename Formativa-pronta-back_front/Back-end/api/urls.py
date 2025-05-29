from django.urls import path
from .views import *

urlpatterns = [
    path('professores/', view=ListcreateUsuario.as_view()),
    path('professores/<int:pk>', view=RetrieveUpdateDestroyUsuario.as_view()),
    path('disciplina/', view=ListcreateDisciplina.as_view()),
    path('disciplina/<int:pk>/', view=RetrieveUpdateDestroyDisciplina.as_view()),
    path('reservaAmbiente/', view=ListcreateReserva.as_view()),
    path('reservaAmbiente/<int:pk>', view=RetrieveUpadateDestroyReserva.as_view()),
    path('professorReservas/', view=Listsalas.as_view()),
    path('professorDisciplinas/', view=Listdisciplinas.as_view()),
    path('token/', view=LoginView.as_view()),
]