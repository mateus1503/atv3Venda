from django.test import TestCase
from .models import Produto, ItemVenda, Venda


class ProdutoTestCase(TestCase):

    def setUp(self):
        # Criar uma instância do modelo Produto
        self.produto = Produto.objects.create(descricao="Produto Teste", valor=10.00)

    def test_produto_creation(self):
        # Testar se o produto foi criado corretamente
        self.assertEqual(self.produto.descricao, "Produto Teste")
        self.assertEqual(self.produto.valor, 10.00)


class ItemVendaTestCase(TestCase):

    def setUp(self):
        # Criar instâncias dos modelos Produto e ItemVenda
        self.produto = Produto.objects.create(descricao="Produto Teste", valor=10.00)
        self.item_venda = ItemVenda.objects.create(quantidade=2, produto=self.produto)

    def test_item_venda_creation(self):
        # Testar se o item de venda foi criado corretamente
        self.assertEqual(self.item_venda.quantidade, 2)
        self.assertEqual(self.item_venda.produto, self.produto)

    def test_item_venda_total(self):
        # Testar o método total do ItemVenda
        expected_total = self.item_venda.quantidade * self.produto.valor
        self.assertEqual(self.item_venda.total(), expected_total)