from django.db import models


class Modelo(models.Model):
    nome = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome} {self.marca} {self.categoria}"