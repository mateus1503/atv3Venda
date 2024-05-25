from django import forms
from .models import ClienteFisico, ClienteJuridico


class ClienteFisicoForm(forms.ModelForm):
    class Meta:
        model = ClienteFisico
        fields = ['nome', 'telefone', 'cpf', 'data_nascimento']


class ClienteJuridicoForm(forms.ModelForm):
    class Meta:
        model = ClienteJuridico
        fields = ['nome', 'telefone', 'cnpj', 'razao_social']
