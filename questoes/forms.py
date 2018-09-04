from django.forms import ModelForm
from questoes.models import Pergunta, Disciplina, Ano, Banca, Nivel, Orgao, Alternativa

class PerguntaForm(ModelForm):
    disciplina = forms.ModelChoiceField(queryset = Disciplina.objects.all(), empty_label="Disciplina...")
    ano = forms.ModelChoiceField(queryset = Ano.objects.all(), empty_label="Ano...")
    banca = forms.ModelChoiceField(queryset = Banca.objects.all(), empty_label="Banca...")
    nivel = forms.ModelChoiceField(queryset = Nivel.objects.all(), empty_label="Nível...")
    orgao = forms.ModelChoiceField(queryset = Orgao.objects.all(), empty_label="Orgão...")
    class Meta:
        model = Pergunta
        fields = ['texto', 'respondida', 'correta', 'reporter', 'disciplina', 'ano', 'banca', 'orgao', 'nivel']


class AlternativaForm(ModelForm):
    class Meta:
        model = Alternativa
        fields = ['texto', 'correta', 'selecionada']