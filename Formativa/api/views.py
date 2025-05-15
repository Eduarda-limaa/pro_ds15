from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UsuarioSerializer, DisciplinaSerializer, ReservaAmbienteSerializer, LoginSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, ListAPIView
from .models import Usuario, Disciplina, ReservaAmbiente
from .permissions import IsGestor, IsUsuario
from rest_framework.permissions import IsAuthenticated

"""

Retrieve -> Consultar um elemento especifico, Exemplo: Consultar o aluno do ID 3 -> GET
127.0.0.1:8000/aluno/3

List -> Consulta tudo. Exemplo a lista de alunos -> GET

Create -> Criar -> POST

Update -> Atualizar -> PUT, PATCH

Destroy -> Apagar/Deletar -> DELETE

"""

# login para os usuarios acessarem o sistema
class LoginView(TokenObtainPairView):
    serializer_class= LoginSerializer

# lista e criação para o gestor criar e verificar professores. 
class ListcreateUsuario(ListCreateAPIView):
    serializer_class = UsuarioSerializer
    permission_classes= [IsGestor]

    def get_queryset(self):
        return Usuario.objects.filter(categoria = 'P')


# consulta, atualização e delete para professores. Com permissão apenas para gestores
class RetrieveUpdateDestroyUsuario(RetrieveUpdateDestroyAPIView):
    serializer_class = UsuarioSerializer
    queryset= Usuario.objects.all()
    permission_classes= [IsGestor]


#lista e criação para o gestor criar e verificar disciplinas.
class ListcreateDisciplina(ListCreateAPIView):
    serializer_class= DisciplinaSerializer
    queryset= Disciplina.objects.all()
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsGestor()]


# consulta, atualização e delete para a disciplina Com permissão apenas para gestores
class RetriveUpadateDestroyDisciplina(RetrieveUpdateDestroyAPIView):
    serializer_class= DisciplinaSerializer
    queryset= Disciplina.objects.all()
    permission_classes= [IsGestor]

#lista e criação para o gestor criar e verificar reservas. 
class ListcreateReserva(ListCreateAPIView):
    serializer_class= ReservaAmbienteSerializer
    queryset= ReservaAmbiente.objects.all()
    permission_classes= [IsGestor]


# consulta, atualização e delete para a reserva Com permissão apenas para gestores
class RetriveUpadateDestroyReserva(RetrieveUpdateDestroyAPIView):
    serializer_class= ReservaAmbienteSerializer
    queryset= ReservaAmbiente.objects.all()
    permission_classes= [IsGestor]


#Visualização de Reservas por Professores
class Listsalas(ListAPIView):
    serializer_class= ReservaAmbienteSerializer

    def get_queryset(self):
        return ReservaAmbiente.objects.filter(professor_responsavel= self.request.user)
   
    permission_classes= [IsUsuario] 


#Visualização de disciplinas por Professores
class Listdisciplinas(ListAPIView):
    serializer_class= DisciplinaSerializer
    
    def get_queryset(self):
        return Disciplina.objects.filter(professor_responsavel= self.request.user)
    
    permission_classes= [IsUsuario]


