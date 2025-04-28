from django.db import models
from django.contrib.auth.models import AbstractUser

# criação da tabela empresa
class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=100)

# criação da tabela usuario
class Usuario(AbstractUser):
    apelido = models.CharField(max_length=100, null=True, blank=True)
    telfone = models.CharField(max_length=100, null=True, blank=True)
    genero = models.CharField(max_length=100, choices=(('M', 'Masculino'), ('F', 'Feminino'), ('N', 'Prefiro não informar')))
    
    escolha_colaborador = (
        ('G', 'Gestor'),
        ('E', 'Estagiário'),
        ('A', 'Aprendiz'),
        ('M', 'Meio Oficial')
    )

    colaborador = models.CharField(max_length=1, choices=escolha_colaborador, default='A')

    REQUIRED_FIELDS = ['colaborador']

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, blank=True)