from django.db import models

# classe com os campos para criação de eventos
class Evento(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    data_hora = models.DateTimeField()
    local = models.CharField(max_length=255, blank=True)
    escolhas_categoria = (
        ('MUSICA', 'Música'),
        ('PALESTRA', 'Palestra'),
        ('WORKSHOP', 'Workshop'),
        ('SEMINARIO', 'Seminario'),
    )
    categoria = models.CharField(max_length=10, choices=escolhas_categoria, blank=True)

    def __str__(self):
        return self.nome    