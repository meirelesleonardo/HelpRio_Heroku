from django.db import models

class Instituicao(models.Model):
    TIPO_INSTITUICAO = (
        ('admin','Administrador'),
        ('coretoraImovel', 'Corretora de Imóvel'),
    )

    InstituicaoId = models.AutoField(primary_key=True)
    NomeFantasia = models.CharField(max_length=800, blank=True, null=True)
    RazaoSocial = models.CharField(max_length=800, blank=True, null=True)
    Cnpj = models.CharField(max_length=800, blank=True, null=True) 
    TipoInstituicao = models.CharField(max_length=100, choices=TIPO_INSTITUICAO, default='coretoraImovel') 
    Dominio = models.CharField(max_length=1000, blank=True, null=True)
    DataCadastro = models.DateTimeField(auto_now_add=True)
    Ativo = models.BooleanField(default=True)
    ficha_instituicao = models.BooleanField(default=True)    

    def __str__(self):
        return self.NomeFantasia