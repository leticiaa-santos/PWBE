from django.shortcuts import render
from .models import Evento
from .serializers import EventoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from datetime import datetime, timedelta

# método GET para listar os eventos existentes e permitir filtros
@api_view(['GET'])
def read_evento(request):
    eventos = Evento.objects.all()

    categoria = request.query_params.get('categoria')
    data_hora = request.query_params.get('data_hora')
    quantidade = request.query_params.get('quantidade')
    ordenacao = request.query_params.get('ordenar')

    if categoria:
        eventos = eventos.filter(categoria__icontains = categoria)

    if data_hora:
        eventos = eventos.filter(data_hora__icontains = data_hora)

    if quantidade:
        eventos = eventos[:int(quantidade)]

    if ordenacao:
        eventos = eventos.order_by('data_hora').values()
    

    serializer = EventoSerializer(eventos, many=True)
    return Response(serializer.data)

# método GET que permite buscar por um evento usando a chave primária
@api_view(['GET'])
def buscar_evento(request, pk):
    try:
        evento = Evento.objects.get(pk=pk)
    except Evento.DoesNotExist:
        return Response({'erro': 'Evento inexistente'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = EventoSerializer(evento)
    return Response(serializer.data)

# método GET para ver os próximos eventos
@api_view(['GET'])
def ver_proximos(request):
    eventos = Evento.objects.all()
    dia = request.query_params.get('dia', '7')
    hoje = datetime.now()
    intervalo = hoje + timedelta(days=int(dia))
    if dia:
        eventos = eventos.filter(data_hora__gte=hoje, data_hora__lte=intervalo)

    serializer = EventoSerializer(eventos, many=True)
    return Response(serializer.data)

# método POST que permite criar um novo evento
@api_view(['POST'])
def create_evento(request):
    if request.method == 'POST':
        serializer = EventoSerializer(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# método PUT que permite atulizar um evento passando todos os parâmetros e mudando o necessário
@api_view(['PUT'])
def update_evento(request, pk):
    try:
        evento = Evento.objects.get(pk=pk)
    except Evento.DoesNotExist:
        return Response({'erro': 'O evento não existe'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = EventoSerializer(evento, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# método DELETE que permite a exclusão do evento com a chave primária
@api_view(['DELETE'])
def delete_evento(resquest, pk):
    try:
        evento = Evento.objects.get(pk=pk)
    except Evento.DoesNotExist:
        return Response({'erro': 'Evento inexistente'}, status=status.HTTP_404_NOT_FOUND)
    
    evento.delete()
    return Response({'Mensagem': f'O evento {evento.nome} foi apagado'}, status=status.HTTP_200_OK)