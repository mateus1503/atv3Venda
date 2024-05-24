from django.db import models


class Produto(models.Model):
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)


class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=16)
    cpf = models.CharField(max_length=11)


class Venda(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)


class ItemVenda(models.Model):
    quantidade = models.PositiveIntegerField()
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    venda = models.ForeignKey(Venda, related_name='itens_venda', on_delete=models.CASCADE)
