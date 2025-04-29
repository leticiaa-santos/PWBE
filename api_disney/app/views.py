from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import UsuarioSerializer, IngressoSerializer, LoginSerializer
from .permissions import IsGestor, IsGestorOuDono
from rest_framework.permissions import IsAuthenticated
from .models import Usuario, Ingresso
from rest_framework_simplejwt.views import TokenObtainPairView

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer


# na disciplina pode fazer o get permissions com o professor ou gestor e se não for nenhum é só o diretor
class UsuarioListCreateAPIView(ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsGestor]

class IngressoRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Ingresso.objects.all()
    serializer_class = IngressoSerializer
    permission_classes = [IsGestorOuDono]

class IngressoListCreateAPIView(ListCreateAPIView):
    queryset = Ingresso.objects.all()
    serializer_class = IngressoSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsGestor()]
    