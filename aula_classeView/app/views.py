from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Piloto, Carro
from .serializars import PilotoSerializer, CarroSerializer
from rest_framework.pagination import PageNumberPagination # type: ignore
from rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class PilotoPaginacao(PageNumberPagination): # fazer paginação para a exibição dos pilotos
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10

class PilotoRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer
    lookup_field = 'pk' # campo que vai ser usado para realizar as ações


    # documentação dos métodos presentes nessa classe

    # sweggar para mostar como pegar um piloto com um ID específico
    @swagger_auto_schema(
        operation_description='Pega o piloto do ID fornecido',
        responses={
            200: PilotoSerializer,
            404: 'Not Found',
            400: 'ERROR'
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    

    # sweggar para mostrar como atualizar um piloto com o ID específico com PUT
    @swagger_auto_schema(
        operation_description='Atualiza o piloto do ID fornecido com o método PUT',
        request_body=PilotoSerializer,
        responses={
            200: PilotoSerializer,
            404: 'Not Found',
            400: 'ERROR'
        }
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    # sweggar para mostrar como atualizar um piloto com o ID específico com PATCH
    @swagger_auto_schema(
        operation_description='Atualiza o piloto do ID fornecido com o método PATCH',
        request_body=PilotoSerializer,
        responses={
            200: PilotoSerializer,
            404: 'Not Found',
            400: 'ERROR'
        }
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    
    # sweggar para mostrar como deletar um piloto com o ID específico
    @swagger_auto_schema(
        operation_description='Deleta o piloto do ID fornecido',
        responses={
            200: PilotoSerializer,
            404: 'Not Found',
            400: 'ERROR'
        }
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class PilotoListCreateAPIView(ListCreateAPIView): # classe que permite a lsitagem e criação de novos pilotos
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer
    pagination_class = PilotoPaginacao

    # documentação com swegger

    # sobre o get, coloca tudo que vai aparecer para poder ver como funciona
    @swagger_auto_schema(
        operation_description='Lista todos os pilotos de Formula 1',
        responses={
            200: PilotoSerializer(many=True),
            400: 'Error'
        },
        manual_parameters=[
            openapi.Parameter(
                'nome', 
                openapi.IN_QUERY,
                description='Filtrar pelo nome do piloto',
                type=openapi.TYPE_STRING
            )
        ]
    )

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    # sweggar para mostrar como criar um piloto novo
    @swagger_auto_schema(
        operation_description='Cria um novo piloto',
        request_body=PilotoSerializer,
        responses={
            201: PilotoSerializer,
            400: 'ERROR'
        }
    )

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def get_queryset(self): # função que permite filtrar os pilotos por nome
        queryset = super().get_queryset()
        nome = self.request.query_params.get('nome')
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        return queryset
    
    def perform_create(self, serializer): # função que permite que apenas os pilotos que fazem parte da equipe determinada possam estar entre os 5 primeiros
        if serializer.validated_data['equipe'] != 'DS16' and serializer.validated_data['classificacao'] <= 5:
            raise serializers.ValidationError('Somente a DS16 pode ficar entre os 5')
        serializer.save()


class CarroPaginacao(PageNumberPagination): # fazer paginação para a exibição dos pilotos
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10

class CarroListCreateAPIView(ListCreateAPIView): # classe que permite a lsitagem e criação de novos carros
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
    pagination_class = CarroPaginacao

    # documentação com swegger

    # sobre o get, coloca tudo que vai aparecer para poder ver como funciona
    @swagger_auto_schema(
        operation_description='Lista todos carros de Formula 1',
        responses={
            200: CarroSerializer(many=True),
            400: 'Error'
        },
        manual_parameters=[
            openapi.Parameter(
                'nome', 
                openapi.IN_QUERY,
                description='Filtrar pelo nome do carro',
                type=openapi.TYPE_STRING
            )
        ]
    )

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    # sweggar para mostrar como criar um carro novo
    @swagger_auto_schema(
        operation_description='Cria um novo carro',
        request_body=CarroSerializer,
        responses={
            201: CarroSerializer,
            400: 'ERROR'
        }
    )

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def get_queryset(self): # função para filtrar o carro por nome
        queryset = super().get_queryset()
        nome = self.request.query_params.get('nome')
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        return queryset        