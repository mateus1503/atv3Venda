from django import forms
from .models import Venda, ItemVenda


class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['usuario']


class ItemVendaForm(forms.ModelForm):
    class Meta:
        model = ItemVenda
        fields = ['produto', 'quantidade']
