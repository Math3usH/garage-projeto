from django.db import models
from core.models import Modelo
from core.models.cor import Cor
from core.models.acessorios import Acessorio


class Veiculo(models.Model):
    ano = models.CharField(max_length=50)
    preco = models.CharField(max_length=50)
    modelo = models.ForeignKey(Modelo,on_delete=models.CASCADE)
    cor = models.ForeignKey(Cor,on_delete=models.CASCADE)
    acessorios = models.ForeignKey(Acessorio,on_delete=models.CASCADE)

    def __str__(self):
        return f"({self.id}) {self.ano} {self.preco} {self.modelo} {self.cor} {self.acessorios}"