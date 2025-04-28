from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializers import UsuarioSerializer
from .permissions import IsGestor

class UsuarioListCreateAPIView(ListCreateAPIView):
    serializer_class = UsuarioSerializer
    permission_classes = [IsGestor]