from django.shortcuts import render
from .models import Venda, Produto, ClienteFisico, ClienteJuridico
from .forms import ClienteFisicoForm, ClienteJuridicoForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def list_venda(request):
    vendas = Venda.objects.order_by('id')
    context = {'vendas': vendas}
    return render(request, 'venda/list_venda.html', context)


def detail_venda(request, venda_id):
    venda = Venda.objects.get(id=venda_id)
    itens_venda = venda.itens_venda.order_by('quantidade')
    context = {'venda': venda, 'itens_venda': itens_venda}
    return render(request, 'venda/detail_venda.html', context)


def list_clientes(request):
    clientes_fisicos = ClienteFisico.objects.all()
    clientes_juridicos = ClienteJuridico.objects.all()

    # Combinar as QuerySets e ordenar por ID
    clientes = sorted(
        list(clientes_fisicos) + list(clientes_juridicos),
        key=lambda cliente: cliente.id
    )
    context = {'clientes': clientes}
    return render(request, 'venda/list_clientes.html', context)


def list_produtos(request):
    produtos = Produto.objects.order_by('id')
    context = {'produtos': produtos}
    return render(request, 'venda/list_produtos.html', context)


def form_fisica(request):
    if request.method != 'POST':
        form = ClienteFisicoForm()
    else:
        form = ClienteFisicoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list_clientes'))

    context = {'form': form}
    return render(request, 'venda/formFisica.html', context)


def form_juridica(request):
    if request.method != 'POST':
        form = ClienteJuridicoForm()
    else:
        form = ClienteJuridicoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list_clientes'))

    context = {'form': form}
    return render(request, 'venda/formJuridica.html', context)
