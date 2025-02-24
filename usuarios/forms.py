from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil, Data

class PerfilForm(forms.ModelForm):
    
    class Meta:
        model = Perfil
        fields = ["nome", "email", "genero", 'endereco']
        widgets = {
            'genero':forms.RadioSelect(),
        }
        

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ["renda_familiar", "num_membros", "despesas_mensais", 
                 "nivel_escolaridade", "tipo_moradia", "situacao_emprego"]
        widgets = {
            'nivel_escolaridade': forms.RadioSelect(),
            'tipo_moradia': forms.Select(attrs={'class': 'form-select'}),
            'situacao_emprego': forms.RadioSelect(),
        }
        labels = {
            'renda_familiar': 'Renda Familiar (R$)',
            'num_membros': 'Número de Membros da Família',
            'despesas_mensais': 'Despesas Mensais (R$)',
            'nivel_escolaridade': 'Nível de Escolaridade',
            'tipo_moradia': 'Tipo de Moradia',
            'situacao_emprego': 'Situação de Emprego'
        }
        help_texts = {
            'renda_familiar': 'Soma da renda de todos os membros da família',
            'despesas_mensais': 'Total de gastos mensais da família'
        }