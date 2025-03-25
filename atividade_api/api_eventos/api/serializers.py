from rest_framework import serializers
from .models import Evento

# classe que será usada para transformar em arquivo JSON
class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'