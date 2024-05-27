from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_venda, name='list_venda'),
    path('venda/<venda_id>', views.detail_venda, name='detail_venda'),
    path('clientes', views.list_clientes, name='list_clientes'),
    path('produtos', views.list_produtos, name='list_produtos'),
    path('form_fisica', views.form_fisica, name='form_fisica'),
    path('form_juridica', views.form_juridica, name='form_juridica'),
]
