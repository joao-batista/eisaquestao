from django.forms import ModelForm, ModelChoiceField, TextInput, Select, Textarea
from questoes.models import Pergunta, Disciplina, Ano, Banca, Nivel, Orgao, Alternativa

class PerguntaForm(ModelForm):
    disciplina = ModelChoiceField(queryset = Disciplina.objects.all(), empty_label="Disciplina...", required=True, widget=Select(attrs={'class':'custom-select'}))
    ano = ModelChoiceField(queryset = Ano.objects.all(), empty_label="Ano...", required=True, widget=Select(attrs={'class':'custom-select'}))
    banca = ModelChoiceField(queryset = Banca.objects.all(), empty_label="Banca...", required=True, widget=Select(attrs={'class':'custom-select'}))
    nivel = ModelChoiceField(queryset = Nivel.objects.all(), empty_label="Nível...", required=True, widget=Select(attrs={'class':'custom-select'}))
    orgao = ModelChoiceField(queryset = Orgao.objects.all(), empty_label="Orgão...", required=True, widget=Select(attrs={'class':'custom-select'}))
    class Meta:
        model = Pergunta
        fields = ['texto', 'disciplina', 'ano', 'banca', 'orgao', 'nivel']
        widgets = {'texto': Textarea(attrs={'class': 'form-control', 'placeholder': 'Pergunta'})}


class AlternativaForm(ModelForm):
    class Meta:
        model = Alternativa
        fields = ['texto', 'correta']
        widgets = {'texto': TextInput(attrs={'class': 'form-control', 'placeholder': 'Alternativa'})}