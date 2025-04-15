from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    biografia = models.TextField(null=True, blank=True)
    idade = models.PositiveIntegerField()
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=255)
    escolaridade = models.CharField(max_length=255, null=True, blank=True)
    quantidade_animal = models.PositiveIntegerField(null=True, blank=True)
    REQUIRED_FIELDS = ['idade', 'telefone', 'endereco']

    def __str__(self):
        return self.username
