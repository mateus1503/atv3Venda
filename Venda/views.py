from django.shortcuts import render, redirect
from .models import Venda, Produto, ItemVenda
from .forms import ProdutoForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib.auth.models import User


def index(request):
    produto = Produto.objects.all()
    context = {'produtos': produto}
    return render(request, 'venda/index.html', context)


@login_required
def list_venda(request, usuario_id):
    if request.user.is_superuser:
        vendas = Venda.objects.order_by('id')
    else:
        usuario = User.objects.get(id=usuario_id)
        vendas = usuario.vendas.order_by('id')
    context = {'vendas': vendas}
    return render(request, 'venda/list_venda.html', context)


@login_required
def detail_venda(request, venda_id):
    venda = Venda.objects.get(id=venda_id)
    itens_venda = venda.itens_venda.order_by('id')
    context = {'venda': venda, 'itens_venda': itens_venda}
    return render(request, 'venda/detail_venda.html', context)


@login_required
def list_usuarios(request):
    if not request.user.is_superuser:
        raise Http404
    usuarios = User.objects.order_by('id')
    context = {'usuarios': usuarios}
    return render(request, 'venda/list_clientes.html', context)


@login_required(login_url=User.is_superuser)
def add_produtos(request):
    if request.method == 'POST':
        form = ProdutoForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProdutoForm()

    context = {'form': form}
    return render(request, 'venda/new_update_produtos.html', context)


@login_required(login_url=User.is_superuser)
def update_produtos(request, produto_id):
    produto = Produto.objects.get(id=produto_id)

    if request.method != 'POST':
        form = ProdutoForm(instance=produto)
    else:
        form = ProdutoForm(instance=produto, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'produto': produto, 'form': form}
    return render(request, 'venda/new_update_produtos.html', context)


@login_required(login_url=User.is_superuser)
def del_produtos(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    produto.delete()
    return redirect('index')


@login_required
def add_to_carrinho(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    produto_id = str(produto_id)

    if 'carrinho' in request.session:
        carrinho = request.session['carrinho']
    else:
        carrinho = {}
    if produto_id in carrinho:
        carrinho[produto_id]['quantidade'] += 1
    else:
        carrinho[produto_id] = {'quantidade': 1, 'descricao': produto.descricao, 'valor': float(produto.valor)}
    request.session['carrinho'] = carrinho
    return redirect('index')


@login_required
def view_carrinho(request):
    carrinho = request.session.get('carrinho', {})
    carrinho_items = []
    total_valor = 0
    for produto_id, item in carrinho.items():
        total_valor += item['quantidade'] * item['valor']
        carrinho_items.append({
            'produto_id': produto_id,
            'descricao': item['descricao'],
            'quantidade': item['quantidade'],
            'valor': item['valor'],
            'total_item': item['quantidade'] * item['valor']
        })

    return render(request, 'venda/list_carrinho.html', {'carrinho_items': carrinho_items, 'total_valor': total_valor})


@login_required
def remove_from_carrinho(request, produto_id):
    carrinho = request.session.get('carrinho', {})
    produto_id = str(produto_id)
    if produto_id in carrinho:
        if carrinho[produto_id]['quantidade'] == 1:
            del carrinho[produto_id]
            request.session['carrinho'] = carrinho
        elif carrinho[produto_id]['quantidade'] > 1:
            carrinho[produto_id]['quantidade'] -= 1
            request.session['carrinho'] = carrinho
    return redirect('view_carrinho')


@login_required
def checkout(request):
    # Recupere os itens do carrinho da sessão
    carrinho = request.session.get('carrinho', {})
    carrinho_items = []

    # Lógica para processar os itens do carrinho e calcular o total
    total_valor = 0
    for produto_id, item_info in carrinho.items():
        try:
            # Recupere as informações detalhadas do produto do banco de dados com base no produto_id
            produto = Produto.objects.get(pk=produto_id)

            # Calcule o preço total deste item no carrinho
            item_total_valor = item_info['quantidade'] * produto.valor

            # Adicione as informações do item à lista de carrinho_items
            carrinho_items.append({
                'produto_id': produto.id,
                'descricao': produto.descricao,
                'quantidade': item_info['quantidade'],
                'valor': produto.valor,
                'total_item': item_total_valor,
            })

            # Atualize o preço total global
            total_valor += item_total_valor
        except Produto.DoesNotExist:
            # Lidar com o caso em que o produto não existe
            continue

    # Verifique se o carrinho está vazio
    if not carrinho_items:
        return redirect('view_carrinho')

    venda = Venda.objects.create(usuario=request.user)
    for item in carrinho_items:
        produto = Produto.objects.get(id=item['produto_id'])
        ItemVenda.objects.create(
            venda=venda,
            produto=produto,
            quantidade=item['quantidade']
        )

    # Limpe o carrinho após a finalização da compra
    request.session['carrinho'] = {}

    # Renderize a página de checkout com as informações do pedido
    return render(request, 'venda/checkout.html', {'carrinho_items': carrinho_items, 'total_valor': total_valor})
