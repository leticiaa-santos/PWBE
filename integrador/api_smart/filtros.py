import django_filters
from .models import Sensores, Ambientes

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