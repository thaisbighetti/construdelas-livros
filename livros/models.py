from django.db import models


# Create your models here.
class Livro(models.Model):
    titulo = models.CharField(max_length=50)
    numero_de_paginas = models.IntegerField()
    editora = models.CharField(max_length=50)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
