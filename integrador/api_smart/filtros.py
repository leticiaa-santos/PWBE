import django_filters
from .models import Sensores, Ambientes, Historico

class FiltroSensor(django_filters.FilterSet):
    sensor_tipo = django_filters.CharFilter(field_name='sensor__sensor', lookup_expr='iexact')

    class Meta:
        model = Sensores
        fields = ['sensor']

class FiltroSig(django_filters.FilterSet):
    ambiente_sig = django_filters.NumberFilter(field_name='sig__sig')

    class Meta:
        model = Ambientes
        fields = ['sig']
        
class FiltroHistorico(django_filters.FilterSet):
    data_inicio = django_filters.DateTimeFilter(field_name="timestamp", lookup_expr='gte')
    data_limite = django_filters.DateTimeFilter(field_name="timestamp", lookup_expr='lte')

    class Meta:
        model = Historico
        fields = ['sensor', 'ambiente', 'data_inicio', 'data_limite']