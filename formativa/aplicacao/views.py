from django.http import Http404
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .models import Usuario, Disciplina, ReservaAmbiente, Sala
from .serializers import UsuarioSerializer, DisciplinaSerializer, ReservaAmbienteSerializer, LoginSerializer, SalaSerializer
from .permissions import IsGestor, IsProfessor, IsDonoOuGestor
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError

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
    
    
    # método que permite a exibição de mensagens se o usuário não existir, ou se ele existir, retornar, em formato json o usuário que foi filtrado
    def retrieve(self, request, *args, **kwargs):
        try:
            usuario = self.get_object()
        except Http404:
            return Response({'message': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(usuario)
        return Response({'usuario ': serializer.data}, status=status.HTTP_200_OK)
    
    
    # método que permite a exibição de mensagens se o usuário não existir, ou se ele existir, retornar, em formato json eles atualizados
    def update(self, request, *args, **kwargs):
        try:
            usuario = self.get_object()
        except Http404:
            return Response({'message': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)

        partial = kwargs.pop('partial', False)
        serializer = self.get_serializer(usuario, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response({'usuario': serializer.data}, status=status.HTTP_200_OK)


    # método que permite a exibição de mensagens se o usuário não existir, ou se ele existir, mostrar que foi excluído
    def destroy(self, request, *args, **kwargs):
        try:
            usuario = self.get_object()
        except Http404:
            return Response({'message': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)

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
    
    
    # método que permite a exibição de mensagens se a disciplina não existir, ou se ela existir, retornar, em formato json a disciplina que foi filtrada
    def retrieve(self, request, *args, **kwargs):
        try:
            disciplina = self.get_object()
        except Http404:
            return Response({'message': 'Disciplina não encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(disciplina)
        return Response({'disciplina ': serializer.data}, status=status.HTTP_200_OK)
    
    
    # método que permite a exibição de mensagens se a disciplina não existir, ou se ela existir, retornar, em formato json ela atualizada
    def update(self, request, *args, **kwargs):
        try:
            disciplina = self.get_object()
        except Http404:
            return Response({'message': 'Disciplina não encontrada'}, status=status.HTTP_404_NOT_FOUND)

        partial = kwargs.pop('partial', False)
        serializer = self.get_serializer(disciplina, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response({'disciplina ': serializer.data}, status=status.HTTP_200_OK)
    
    
    # método que permite a exibição de mensagens para o usuário se a disciplina não existir, ou se ela existir, mostrar que foi excluída
    def destroy(self, request, *args, **kwargs):
        try:
            disciplina = self.get_object()
        except Http404:
            return Response({'message': 'Disciplina não encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.perform_destroy(disciplina)
        return Response({'detail': f'Disciplina "{disciplina.nome}" excluída com sucesso.'}, status=status.HTTP_200_OK)


# listagem das disciplinas (professor)
class DisciplinaProfessorList(ListAPIView):
    serializer_class = DisciplinaSerializer
    permission_classes = [IsProfessor]

    def get_queryset(self):
        return Disciplina.objects.filter(professor=self.request.user) # filtra todas as disciplinas do usuário logado (professor, no caso)
    
# permite criar e listar as reservas, qualquer um pode ver todas, só o gestor pode criar
class ReservaAmbienteListCreate(ListCreateAPIView):
    queryset = ReservaAmbiente.objects.all()
    serializer_class = ReservaAmbienteSerializer

    # esse método permite a validação das reservas
    # ele verifica se já existe a reserva com a data de início ou término, a sala e o período e se existir ele exibe um mensagem de erro
    def perform_create(self, serializer):
        print("Não foi possível fazer a reserva")
        data_inicio = serializer.validated_data.get('data_inicio')
        data_termino = serializer.validated_data.get('data_termino')
        sala_reservada = serializer.validated_data.get('sala_reservada')
        periodo = serializer.validated_data.get('periodo')

        reserva = ReservaAmbiente.objects.filter(
            sala_reservada = sala_reservada, 
            data_inicio__lte= data_termino, 
            data_termino__gte=data_inicio, 
            periodo = periodo
        ).exists()

        if reserva:
            raise ValidationError("Não é possível realizar essa reserva, já existe uma!")

        serializer.save()

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


    # método que permite a exibição de mensagens se a reserva não existir, ou se ela existir, retornar, em formato json a disciplina que foi filtrada
    def retrieve(self, request, *args, **kwargs):
        try:
            reserva = self.get_object()
        except Http404:
            return Response({'message': 'Reserva não encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(reserva)
        return Response({'reserva ': serializer.data}, status=status.HTTP_200_OK)
    
    
    # método que permite a exibição de mensagens se a reserva não existir, ou se ela existir, retornar, em formato json ela atualizada
    def update(self, request, *args, **kwargs):
        try:
            reserva = self.get_object()
        except Http404:
            return Response({'message': 'Reserva não encontrada'}, status=status.HTTP_404_NOT_FOUND)

        partial = kwargs.pop('partial', False)
        serializer = self.get_serializer(reserva, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response({'reserva ': serializer.data}, status=status.HTTP_200_OK)
    
    
    # método que permite a exibição de mensagens para o usuário se a reserva não exitir, ou se ela existir, mostrar que foi excluída
    def destroy(self, request, *args, **kwargs):
        try:
            reserva = self.get_object()
            nome_sala = reserva.sala_reservada.nome
        except Http404:
            return Response({'message': 'Reserva não encontrada'}, status=status.HTTP_404_NOT_FOUND)

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

# permite criar e listar as salas, qualquer um pode ver todas, só o gestor pode criar
class SalaListCreate(ListCreateAPIView):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

    # se for método get qualquer usuário pode visualizar, se for outro método só o gestor pode realizar a ação
    def get_permissions(self):
        if self.request.method == 'GET':
            return[IsAuthenticated()]
        return [IsGestor()]
    
# GET, PUT, PATCH e DELETE que é permitido somente para o gestor
# ver, atualizar e deletar uma sala específica
class SalaRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer
    permission_classes = [IsGestor]
    
    
    # método que permite a exibição de mensagens se a sala não existir, ou se ela existir, retornar, em formato json a sala que foi filtrada
    def retrieve(self, request, *args, **kwargs):
        try:
            sala = self.get_object()
        except Http404:
            return Response({'message': 'Sala não encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(sala)
        return Response({'sala ': serializer.data}, status=status.HTTP_200_OK)
    
    
    # método que permite a exibição de mensagens se a sala não existir, ou se ela existir, retornar, em formato json ela atualizada
    def update(self, request, *args, **kwargs):
        try:
            sala = self.get_object()
        except Http404:
            return Response({'message': 'Sala não encontrada'}, status=status.HTTP_404_NOT_FOUND)

        partial = kwargs.pop('partial', False)
        serializer = self.get_serializer(sala, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response({'sala ': serializer.data}, status=status.HTTP_200_OK)
    

    # método que permite a exibição de mensagens para o usuário se a reserva não exitir, ou se ela existir, mostrar que foi excluída
    def destroy(self, request, *args, **kwargs):
        try:
            sala = self.get_object()
        except Http404:
            return Response({'message': 'Sala não encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.perform_destroy(sala)
        return Response({'detail': f'Sala "{sala.nome}" excluída com sucesso.'}, status=status.HTTP_200_OK)