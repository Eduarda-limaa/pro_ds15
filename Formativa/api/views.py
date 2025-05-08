from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UsuarioSerializer, DisciplinaSerializer, ReservaAmbienteSerializer, LoginSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
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


# consulta, atualização e delete para o usuario/professores. Com permissão apenas para gestores
class RetrieveUpdateDestroyUsuario(RetrieveUpdateDestroyAPIView):
    serializer_class = UsuarioSerializer
    queryset= Usuario.objects.all()
    permission_classes= [IsGestor]


#ista e criação para o gestor criar e verificar disciplina. Com possibilidade de visualização da lista para os professores
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
    permission_classes= [IsUsuario]


# consulta, atualização e delete para a reserva Com permissão apenas para gestores
class RetriveUpadateDestroyReserva(RetrieveUpdateDestroyAPIView):
    serializer_class= ReservaAmbienteSerializer
    queryset= ReservaAmbiente.objects.all()
    permission_classes= [IsGestor]



    

