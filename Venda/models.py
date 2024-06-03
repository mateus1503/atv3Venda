from django.db import models
from django.contrib.auth.models import User


class Produto(models.Model):
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produto_imagens/')

    def __str__(self):
        return self.descricao


class Venda(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, related_name='vendas', on_delete=models.CASCADE)

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
