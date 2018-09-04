from django.core.management.base import BaseCommand, CommandError
from questoes.models import Disciplina, Ano, Banca, Orgao, Nivel 

class Command(BaseCommand):
    help = 'script para popular as tabelas de dominio'

    disciplinas = ['Português', 'Direito Administrativo', 'Direito Constitucional', 'Direito Penal', 'Direito Processual Penal', 'Direito Civil', 'Noções de Informática', 'Raciocínio Lógico', 'Matemática', 'Direito do Trabalho', 'Administração Geral', 'Direito Tributário', 'Direito Processual do Trabalho', 'Administração Pública']
    bancas = ['CESPE', 'CESGRANRIO', 'CONSULPLAN', 'FCC', 'FGV', 'VUNESP', 'ESAF', 'IPAD', 'QUADRIX']
    anos = ['2000', '2001', '2002', '2003', '2004', '2005', '2006','2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
    orgaos = ['TRT', 'TRF', 'TCE', 'Petrobrás', 'CGU', 'Polícia Militar']
    niveis =['Nível Médio', 'Nível Superior']

    def handle(self, *args, **options):
        self.popular_tabelas()

    def popular_tabelas(self):
        self.popular_tabela(Disciplina, self.disciplinas)
        self.popular_tabela(Ano, self.anos)
        self.popular_tabela(Banca, self.bancas)
        self.popular_tabela(Nivel, self.niveis)
        self.popular_tabela(Orgao, self.orgaos)
        self.stdout.write('Registros inseridos com sucesso!')

    def popular_tabela(self, objeto, lista):
        for descricao in lista:
            novo_objeto = self.criar_objeto(objeto, descricao)
            try:
                novo_objeto.save()
            except:
                self.stdout.write('O registro "%s" já existe na base de dados' % descricao)

    def criar_objeto(self, objeto, descricao):
        if (objeto.__name__ == 'Disciplina'):
            return Disciplina(descricao = descricao)
        if (objeto.__name__ == 'Ano'):
            return Ano(descricao = descricao)
        if (objeto.__name__ == 'Nivel'):
            return Nivel(descricao = descricao)
        if (objeto.__name__ == 'Orgao'):
            return Orgao(descricao = descricao)
        if (objeto.__name__ == 'Banca'):
            return Banca(descricao = descricao)