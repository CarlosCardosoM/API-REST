from django.db import models

class Monografia(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    orientador = models.CharField(max_length=100)
    coorientador = models.CharField(max_length=100, blank=True, null=True)
    resumo = models.TextField()
    abstract = models.TextField()
    palavras_chave = models.CharField(max_length=200)
    data_defesa = models.DateField()
    arquivo = models.FileField(..., blank=True, null=True)

    def __str__(self):
        return self.titulo
