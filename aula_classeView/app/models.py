from django.db import models

class Piloto(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.PositiveIntegerField()
    classificacao = models.PositiveIntegerField()
    equipe = models.CharField(max_length=255)

    def __str__ (self):
        return f'{self.nome} está na posição {self.classificacao}'


class Carro(models.Model):
    nome = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    valocidade_maxima = models.PositiveIntegerField()
    escolha_cores = (
        ('VERMELHO', 'Vermelho'),
        ('ROSA', 'rosa'),
        ('BRANCO', 'branco'),
        ('PRETO', 'preto'),
        ('VERDE', 'verde'),
        ('MARROM', 'marrom'),
        ('ROXO', 'roxo'),
        ('CINZA', 'cinza'),
        ('DOURADO', 'dourado')
    )
    cor = models.CharField(max_length=50, choices=escolha_cores)
    piloto = models.ForeignKey(Piloto, on_delete=models.CASCADE)