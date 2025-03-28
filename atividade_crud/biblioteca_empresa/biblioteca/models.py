from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    autores = models.CharField(max_length=255)
    ano = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name_plural = "Livros"