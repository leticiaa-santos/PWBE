from rest_framework import serializers
from .models import Usuario, Empresa, Ingresso
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class LoginSerializer(TokenObtainPairSerializer): # obter par do token para a manipulação
    def validate(self, attrs):
        data = super().validate(attrs) # super chama a função validate 
        data['usuario'] = { # campo novos para ver além dos de padrão
            'id': self.user.id,
            'username': self.user.username,
        }
        return data # retorna os dados
    
class IngressoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingresso
        fields = '__all__'