from django.forms import ModelForm
from apps.ficha_imovel.models import Condominio, Proprietario

class CriarLaudo(ModelForm):
    #Condominio = forms.CharField()
    class Meta:
        model = Condominio
        fields = '__all__'