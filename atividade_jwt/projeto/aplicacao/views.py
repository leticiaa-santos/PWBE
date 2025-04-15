from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .serializers import UsuarioSerializer

@api_view(['POST'])
def criar_usuario(request):
    username = request.data.get('username')
    senha = request.data.get('senha')
    biografia = request.data.get('biografia')
    idade = request.data.get('idade')
    telefone = request.data.get('telefone')
    endereco = request.data.get('endereco')
    escolaridade = request.data.get('escolaridade')
    quantidade_animal = request.data.get('quantidade_animal')

    if not username or not senha or not idade or not telefone:
        return Response({'Erro': 'Campos obrigatórios incompletos'}, status=status.HTTP_400_BAD_REQUEST)
    
    if Usuario.objects.filter(username=username).exists():
        return Response({'Erro': f'Username {username} já existe'}, status=status.HTTP_400_BAD_REQUEST)
    
    usuario = Usuario.objects.create_user(
        username=username,
        password=senha,
        biografia=biografia,
        idade=idade,
        telefone=telefone,
        endereco=endereco,
        escolaridade=escolaridade,
        quantidade_animal=quantidade_animal

    )
    return Response({'Mensagem': f'Usuário {username} criado com sucesso'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def logar_usuario(request):
    username = request.data.get('username')
    senha = request.data.get('senha')

    usuario = authenticate(username=username, password=senha)

    if usuario:
        refresh = RefreshToken.for_user(usuario)
        return Response({
            'acesso': str(refresh.access_token),
            'refresh': str(refresh)
        }, status=status.HTTP_200_OK)
    else:
        return Response({'Erro': 'Usuário ou/e senha incorreto(s)'}, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read(request):
    usuarios = Usuario.objects.all()
    serializer = UsuarioSerializer(usuarios, many=True)
    return Response(serializer.data)

# método PUT que permite atulizar um evento passando todos os parâmetros e mudando o necessário
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_usuario(request, pk):
    try:
        usuario = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return Response({'erro': 'O usuário não existe'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = UsuarioSerializer(usuario, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# método DELETE que permite a exclusão do evento com a chave primária
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_usuario(resquest, pk):
    try:
        usuario = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        return Response({'erro': 'Usuário inexistente'}, status=status.HTTP_404_NOT_FOUND)
    
    usuario.delete()
    return Response({'Mensagem': f'O usuário {usuario.username} foi apagado'}, status=status.HTTP_200_OK)