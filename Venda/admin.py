from django.contrib import admin
from .models import Produto, Cliente, Venda, ItemVenda


admin.site.register(Produto)
admin.site.register(Cliente)
admin.site.register(Venda)
admin.site.register(ItemVenda)
