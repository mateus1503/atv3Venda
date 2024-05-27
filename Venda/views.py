from django.shortcuts import render
from .models import Venda, Produto
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User


def list_venda(request):
    vendas = Venda.objects.order_by('id')
    context = {'vendas': vendas}
    return render(request, 'venda/list_venda.html', context)


def detail_venda(request, venda_id):
    venda = Venda.objects.get(id=venda_id)
    itens_venda = venda.itens_venda.order_by('quantidade')
    context = {'venda': venda, 'itens_venda': itens_venda}
    return render(request, 'venda/detail_venda.html', context)


def list_usuarios(request):
    usuarios = User.objects.order_by('id')
    context = {'clientes': usuarios}
    return render(request, 'venda/list_clientes.html', context)


def list_produtos(request):
    produtos = Produto.objects.order_by('id')
    context = {'produtos': produtos}
    return render(request, 'venda/list_produtos.html', context)
