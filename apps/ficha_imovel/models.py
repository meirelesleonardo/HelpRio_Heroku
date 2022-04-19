from operator import mod
from django.db import models
from django.urls import clear_url_caches
from apps.instituicao.models import Instituicao
from apps.models.BaseModels import CreatedBy, TimeStampedModel, UuidModel
from users.models import User


class Condominio(models.Model):
    CondominioId = models.AutoField(primary_key=True)
    Condominio = models.CharField('Condomínio',max_length=1000, blank=True, null=True)
    Tipo = models.CharField(max_length=100, blank=True, null=True)
    Bairro = models.CharField(max_length=100, blank=True, null=True)
    Endereco = models.CharField('Endereço',max_length=1000, blank=True, null=True)
    Localizacao = models.CharField('Localização',max_length=1000, blank=True, null=True)
    NomeDoEdificio = models.CharField('Nome do edifício',max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.Condominio

class Proprietario(models.Model):
    ProprietarioId = models.AutoField(primary_key=True)
    nome = models.CharField('Proprietário',max_length=1000, blank=True, null=True)
    TelCelular = models.CharField('Celular',max_length=100, blank=True, null=True)
    TelResidencial = models.CharField('Res.',max_length=500, blank=True, null=True)
    TelComercial = models.CharField('Com.',max_length=500, blank=True, null=True)
    E_mail = models.CharField('E-mail',max_length=500, blank=True, null=True)
    Conjge = models.CharField('Cônjuge',max_length=500, blank=True, null=True)
    ConjugeCel = models.CharField('Cel',max_length=500, blank=True, null=True)
    ConjugeE_mail = models.CharField('E-mail',max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.nome

class FichaImovel(models.Model):
    POSICAO = (
        (0,''),
        (1,'Fundos'),
        (2, 'Frente'),
        (3, 'Lateral'),
    )

    SOL = (
        ('M','Manhã'),
        ('T', 'Tarde'),
    )

    SITUACAO_IMOVEL = (
        (0,'Vazio'),
        (1, 'Ocupado'),        
    )

    SIM_NAO = (
        (0,'Sim'),
        (1, 'Nao'),        
    )

    FichaImovelId = models.AutoField(primary_key=True)
    CodigoUnico = models.CharField('CÓDIGO UN.',max_length=100, blank=True, null=True)
    
    CantoDePedra = models.BooleanField('Canto de Pedra',default=False)
    MotivoCantoDePedra = models.CharField('Motivo Canto de Pedra',max_length=300, blank=True, null=True)

    Posicao = models.IntegerField('Posição',choices=POSICAO, default=0)
    Sol = models.CharField(max_length=1, choices=SOL, blank=True, null=True)
    SituacaoImovel = models.IntegerField('Imóvel',choices=SITUACAO_IMOVEL, blank=True, null=True)

    Agendar = models.CharField(max_length=300, blank=True, null=True)
    Placa = models.CharField(max_length=100, blank=True, null=True)
    Chave = models.CharField(max_length=100, blank=True, null=True)

    Quartos = models.IntegerField(blank=True, null=True)
    Suites = models.IntegerField('Suítes',blank=True, null=True)
    Banheiros = models.IntegerField('Total de Banheiros',blank=True, null=True)
    Vagas = models.IntegerField(blank=True, null=True)
    Subsolo = models.IntegerField(choices=SIM_NAO, default=1)
    ElevadorSocial = models.BooleanField('Elev Soc.',default=True)
    ElevadorServico = models.BooleanField('Elev Serv.',default=True)
    NumeroPavmento = models.IntegerField('No Pav',blank=True, null=True)
    UnidadeAndar = models.IntegerField('Unid./Andar',blank=True, null=True)
    Idade = models.IntegerField(blank=True, null=True)

    AreaTerreno = models.FloatField('Área do terreno',blank=True, null=True)
    AreaConstruida = models.FloatField('Área construída',blank=True, null=True)
    ValorCondominio = models.FloatField('Valor Cond.',blank=True, null=True)
    HidrometroIndvidual = models.IntegerField('Hidrômetro individual',choices=SIM_NAO, default=0)
    IptuAtual = models.FloatField('IPTU Anual',blank=True, null=True)
    NumeroInscricao = models.IntegerField('No de Inscrição',blank=True, null=True)

    ValorVenda = models.FloatField('Valor Venda',blank=True, null=True)
    EntregaEm = models.DateField('E ntrega em',blank=True, null=True)
    AceitaPermuta = models.IntegerField('Aceita Permuta',choices=SIM_NAO, default=1)
    Aonde = models.CharField(max_length=1000, blank=True, null=True)
    MotivoDavenda = models.CharField('Motivo da venda',max_length=1000, blank=True, null=True)
    CondicoesObs = models.CharField('Condições/Obs.',max_length=1000, blank=True, null=True)

    OnibusVan = models.IntegerField('Ônibus/Van',choices=SIM_NAO, default=1)
    Balsa = models.IntegerField(choices=SIM_NAO, default=1)
    Dependencia = models.IntegerField('Dependência',choices=SIM_NAO, blank=True, null=True)
    FotosImovel = models.IntegerField('Fotos imóvel',choices=SIM_NAO, blank=True, null=True)
    FotosCondominio = models.IntegerField('Fotos cond.',choices=SIM_NAO, blank=True, null=True)
    PlayGround = models.IntegerField('Play Ground',choices=SIM_NAO, blank=True, null=True)
    Piscina = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    Academia = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    AreaGourmet = models.IntegerField('Área Gourmet',choices=SIM_NAO, blank=True, null=True)
    Sauna = models.IntegerField(choices=SIM_NAO, blank=True, null=True)
    SalaoDeFestas = models.IntegerField('Salão de festas',choices=SIM_NAO, blank=True, null=True)
    QuadraSports = models.IntegerField('Quadra sports',choices=SIM_NAO, blank=True, null=True)

    Opcionista =  models.CharField(max_length=100, blank=True, null=True)
    Comissao = models.FloatField('Comissão',blank=True, null=True)
    CaptacaoFicha = models.FloatField('Captação Ficha',blank=True, null=True) 
    outro = models.CharField(max_length=1000, blank=True, null=True)
    HabiteSe = models.IntegerField('Habite-se',choices=SIM_NAO, blank=True, null=True)
    DocumentacaoNaEmpresa = models.IntegerField('Documentação na empresa',choices=SIM_NAO, blank=True, null=True)
    qual =  models.CharField(max_length=500, blank=True, null=True)
    Descricao = models.TextField('Descrição',max_length=20000, blank=True, null=True)

    DataAtualizacao = models.DateTimeField('Data Atualização',auto_now=True)
    AtualizacaoObs = models.CharField('Atualização Obs.',max_length=20000, blank=True, null=True)
    
    DataUltimaModificacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.CodigoUnico

class Laudo(
    UuidModel,
    TimeStampedModel,
    CreatedBy,
    Condominio,
    Proprietario,
    FichaImovel,
    Instituicao
    ):

    LaudoId = models.AutoField(primary_key=True)
    DataCadastroLaudo = models.DateTimeField('Data do laudo',auto_now_add=True)

    def __str__(self):
        return self.LaudoId