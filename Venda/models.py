from django.db import models
from django.db.models import Sum, F


class Produto(models.Model):
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.descricao


class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=16)
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.nome


class Venda(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def total_venda(self):
        total = 0
        for item in self.itens_venda.all():
            total += item.get_total()
        return total


class ItemVenda(models.Model):
    quantidade = models.PositiveIntegerField()
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    venda = models.ForeignKey(Venda, related_name='itens_venda', on_delete=models.CASCADE)

    def get_total(self):
        return self.quantidade * self.produto.valor
