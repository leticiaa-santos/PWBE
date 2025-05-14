from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .models import Usuario, Disciplina, ReservaAmbiente, Sala
from .serializers import UsuarioSerializer, DisciplinaSerializer, ReservaAmbienteSerializer, LoginSerializer, SalaSerializer
from .permissions import IsGestor, IsProfessor, IsDonoOuGestor
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status

# GET e POST do usuário permitido somente para o Gestor
class UsuarioListCreate(ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsGestor]

# GET, PUT, PATCH e DELETE que é permitido somente para o gestor
# ver, atualizar e deletar um usuario específico
class UsuarioRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsGestor]
    lookup_field = 'pk' # por qual campo procura
    
    def destroy(self, request, *args, **kwargs):
        usuario = self.get_object()
        print(f'Excluindo disciplina: {usuario.username}')
        self.perform_destroy(usuario)
        return Response({'detail': f'Usuário "{usuario.username}" excluído com sucesso.'}, status=status.HTTP_200_OK)


# ver todas as displinas e criar uma nova disciplina (apenas o gestor pode fazer)
class DisciplinaListCreate(ListCreateAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    lookup_field = 'pk'

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsGestor()]
    
    
# GET, PUT, PATCH e DELETE que é permitido somente para o gestor
# ver, atualizar e deletar uma disciplina específica
class DisciplinaRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    permission_classes = [IsGestor]
    lookup_field = 'pk'
    
    def destroy(self, request, *args, **kwargs):
        disciplina = self.get_object()
        print(f'Excluindo disciplina: {disciplina.nome}')
        self.perform_destroy(disciplina)
        return Response({'detail': f'Disciplina "{disciplina.nome}" excluída com sucesso.'}, status=status.HTTP_200_OK)


# listagem das disciplinas (professor)
class DisciplinaProfessorList(ListAPIView):
    serializer_class = DisciplinaSerializer
    permission_classes = [IsProfessor]

    def get_queryset(self):
        return Disciplina.objects.filter(professor=self.request.user) # filtra todas as disciplinas do usuário logado (professor no caso)
    
# permite criar e listar as reservas, qualquer um pode ver todas, só o gestor pode criar
class ReservaAmbienteListCreate(ListCreateAPIView):
    queryset = ReservaAmbiente.objects.all()
    serializer_class = ReservaAmbienteSerializer

    # se for método get qualquer usuário pode visualizar, se for outro método só o gestor pode realizar a ação
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsGestor()]
    

    # permite fazer uma consulta para ver as reservas de um professor específico pelo ID
    def get_queryset(self):
        queryset = super().get_queryset()
        professor_id = self.request.query_params.get('professor', None)
        if professor_id: 
            queryset = queryset.filter(professor_id=professor_id)
        return queryset
    
# vai permitir que o gestor ou o dono da reserva consiga editar as reservas
class ReservaAmbienteRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = ReservaAmbiente.objects.all()
    serializer_class = ReservaAmbienteSerializer
    permission_classes = [IsDonoOuGestor]
    lookup_field = 'pk'
    
    def destroy(self, request, *args, **kwargs):
        reserva = self.get_object()
        nome_sala = reserva.sala_reservada.nome
        self.perform_destroy(reserva)
        return Response({'detail': f'Reserva na sala "{nome_sala}" excluída com sucesso.'}, status=status.HTTP_200_OK)


# permite que apenas o professor pode ver suas próprias reservas
class ReservaAmbienteProfessorList(ListAPIView):
    serializer_class = ReservaAmbienteSerializer
    permission_classes = [IsProfessor]

    # filtrar as reservas do professor específico
    def get_queryset(self):
        return ReservaAmbiente.objects.filter(professor=self.request.user)

# view que vai permitir o usuário logar e ter os tokens
class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer


class SalaListCreate(ListCreateAPIView):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return[IsAuthenticated()]
        return [IsGestor()]
    

class SalaRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer
    permission_classes = [IsGestor]
