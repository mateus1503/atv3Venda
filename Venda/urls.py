from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vendas/<usuario_id>', views.list_venda, name='list_venda'),
    path('venda/<venda_id>', views.detail_venda, name='detail_venda'),
    path('usuarios', views.list_usuarios, name='list_usuarios'),
    path('produtos', views.list_produtos, name='list_produtos'),
]
