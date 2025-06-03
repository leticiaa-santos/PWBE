from django.shortcuts import render, get_object_or_404
from .models import Sensores, Ambientes, Historico
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import SensoresSerializer, AmbientesSerializer, HistoricoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .utils import ler_excel, exportar_excel
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from .filtros import FiltroSensor, FiltroSig

class SensoresListCreate(ListCreateAPIView):
    queryset = Sensores.objects.all()
    serializer_class = SensoresSerializer
    permission_classes = [IsAuthenticated]


class SensoresRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Sensores.objects.all()
    serializer_class = SensoresSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend]
    filterset_class = FiltroSensor

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

    filter_backends = [DjangoFilterBackend]
    filterset_class = FiltroSig


class HistoricoListCreate(ListCreateAPIView):
    queryset = Historico.objects.all()
    serializer_class = HistoricoSerializer
    permission_classes = [IsAuthenticated]


class HistoricoRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Historico.objects.all()
    serializer_class = HistoricoSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]


class ImportarExcel(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            ler_excel(request)
            return Response({"menssagem": "Dados importados com sucesso"}, status=status.HTTP_200_OK)
        except Exception:
            return Response({"mensagem": "Você não tem a devida autorização para realizar a importação dos dados"}, status=status.HTTP_401_UNAUTHORIZED)


class ExportarExcel(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            return exportar_excel(request)
        except Exception:
            return Response({"mensagem": "Você não tem a devida autorização para realizar a exportação dos dados"}, status=status.HTTP_401_UNAUTHORIZED)