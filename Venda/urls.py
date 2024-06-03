from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vendas/<usuario_id>/', views.list_venda, name='list_venda'),
    path('venda/<venda_id>/', views.detail_venda, name='detail_venda'),
    path('usuarios/', views.list_usuarios, name='list_usuarios'),
    path('add_produtos/', views.add_produtos, name='add_produtos'),
    path('update_produtos/<produto_id>/', views.update_produtos, name='update_produtos'),
    path('del_produtos/<produto_id>', views.del_produtos, name='del_produtos'),
    path('add_to_carrinho/<produto_id>/', views.add_to_carrinho, name='add_to_carrinho'),
    path('view_carrinho/', views.view_carrinho, name='view_carrinho'),
    path('remove_from_carrinho/<produto_id>', views.remove_from_carrinho, name='remove_from_carrinho'),
    path('checkout/', views.checkout, name='checkout'),
]
