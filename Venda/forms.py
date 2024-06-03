from django import forms
from .models import Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['descricao', 'valor', 'imagem']
        labels = {'descricao': 'Descrição', 'valor': 'Valor', 'imagem': 'Imagem'}
