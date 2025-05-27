from django.shortcuts import render, get_object_or_404
from .models import Sensores, Ambientes, Historico
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import SensoresSerializer, AmbientesSerializer, HistoricoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

class SensoresListCreate(ListCreateAPIView):
    queryset = Sensores.objects.all()
    serializer_class = SensoresSerializer
    permission_classes = [IsAuthenticated]


class SensoresRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Sensores.objects.all()
    serializer_class = SensoresSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]

    #mensagem que foi atualizado
    def update(self, request, *args, **kwargs):
        sensor = super().update(request, *args, **kwargs)
        return Response({
            'mensagem': 'Sensor atualizado com sucesso!',
            'dados': sensor.data
        }, status=status.HTTP_200_OK)

    #mensagem pra quando o user é deletado
    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({
            'mensagem': 'Sensor deletado com sucesso!'
        }, status=status.HTTP_204_NO_CONTENT)


class AmbienteListCreate(ListCreateAPIView):
    queryset = Ambientes.objects.all()
    serializer_class = AmbientesSerializer
    permission_classes = [IsAuthenticated]


class AmbienteRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Ambientes.objects.all()
    serializer_class = AmbientesSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]


class HistoricoListCreate(ListCreateAPIView):
    queryset = Historico.objects.all()
    serializer_class = HistoricoSerializer
    permission_classes = [IsAuthenticated]


class HistoricoRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Historico.objects.all()
    serializer_class = HistoricoSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]