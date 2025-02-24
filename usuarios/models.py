from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.db import models as md

class Perfil(md.Model):
    usuario = md.OneToOneField(User, on_delete=md.CASCADE, related_name="perfil")
    nome = md.CharField(max_length=255, blank=True, null=True)
    endereco = md.CharField(max_length=255, blank=True, null=True)
    email = md.EmailField(max_length=255, blank=True, null=True)
    genero = md.CharField(
        max_length=20,
        choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')],
        blank=True,
        null=True
        )
    
class Data(md.Model):
    TIPO_MORADIA = [
        ('ALUGADA', 'Alugada'),
        ('PROPRIA', 'Própria'),
        ('CEDIDA', 'Cedida'),
        ('INVADIDA', 'Invadida')
    ]
    
    SITUACAO_EMPREGO = [
        ('EMPREGADO', 'Empregado'),
        ('DESEMPREGADO', 'Desempregado'),
        ('AUTONOMO', 'Autônomo'),
        ('APOSENTADO', 'Aposentado')
    ]
    usuario = md.OneToOneField(User, on_delete=md.CASCADE, related_name='Data')
    renda_familiar = md.FloatField(help_text="Renda total da família em reais")
    num_membros = md.PositiveIntegerField(help_text='Número de membros na família')
    despesas_mensais = md.FloatField(help_text='Despesas mensais da família em reais')
    tipo_moradia = md.CharField(max_length=20, choices=TIPO_MORADIA)
    situacao_emprego = md.CharField(max_length=20, choices=SITUACAO_EMPREGO)
    nivel_escolaridade = md.CharField(max_length=50,
                                          choices=[
        ('FUND', 'Ensino Fundamental'),
        ('MED', 'Ensino Médio'),
        ('SUP', 'Ensino Superior'),
        ('POS', 'Pós-graduação'),
        ('OUT', 'Outro'),
    ])

                                          
    
    
    
    
        
    