from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_venda, name='list_venda'),
    path('venda/<venda_id>', views.detail_venda, name='detail_venda'),
]
