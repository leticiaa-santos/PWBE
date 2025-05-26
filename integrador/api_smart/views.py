from django.shortcuts import render, get_object_or_404
from .models import Sensores, Ambientes, Historico
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import SensoresSerializer, AmbientesSerializer, HistoricoSerializer

class SensoresListCreate(ListCreateAPIView):
    queryset = Sensores.objects.all()
    serializer_class = SensoresSerializer



class SensoresRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Sensores.objects.all()
    serializer_class = SensoresSerializer
    lookup_field = 'pk'

    # futuro código para os filtros do sensor
    def get_object(self):
        sensor = self.kwargs.get('sensor')
        timestamp = self.kwargs.get('timestamp')
        return get_object_or_404(Sensores, sensor=sensor, timestamp=timestamp)



class AmbienteListCreate(ListCreateAPIView):
    queryset = Ambientes.objects.all()
    serializer_class = AmbientesSerializer


class AmbienteRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Ambientes.objects.all()
    serializer_class = AmbientesSerializer
    lookup_field = 'pk'


class HistoricoListCreate(ListCreateAPIView):
    queryset = Historico.objects.all()
    serializer_class = HistoricoSerializer


class HistoricoRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Historico.objects.all()
    serializer_class = HistoricoSerializer
    lookup_field = 'pk'