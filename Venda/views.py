from django.shortcuts import render
from .models import Venda


def list_venda(request):
    vendas = Venda.objects.order_by('data')
    context = {'vendas': vendas}
    return render(request, 'venda/list_venda.html', context)


def detail_venda(request, venda_id):
    venda = Venda.objects.get(id=venda_id)
    itens_venda = venda.itens_venda.order_by('quantidade')
    context = {'venda': venda, 'itens_venda': itens_venda}
    return render(request, 'venda/detail_venda.html', context)
