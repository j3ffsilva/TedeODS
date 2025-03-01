import re
from classifiers.base_classifier import BaseODSClassifier

class ODS04Classifier(BaseODSClassifier):
    def __init__(self):
        super().__init__(4)

    def get_padroes(self):
        """Define os padrões de busca como uma lista de expressões regulares."""

        # Termos obrigatórios: {escola} OU {educação} OU {educacional}
        termos_obrigatorios = r'(?=.*\b(?:escola|educa[çc][ãa]o|educacional)\b)'

        # Termos específicos simples (buscados diretamente)
        termos_simples = [
            r'\bfrequ[êe]ncia\s+escolar\b',
            r'\bmatr[íi]cula\s+escolar\b',
            r'\beduca[çc][ãa]o\s+inclusiva\b',
            r'\bdesigualdade\s+educacional\b',
            r'\bqualidade\s+educacional\b',
            r'\bmatr[íi]cula\s+educacional\b',
            r'\balfabetiza[çc][ãa]o\s+de\s+adultos\b',
            r'\btaxa\s+de\s+numeramento\b',
            r'\bambiente\s+educacional\b',
            r'\bacesso\s+educacional\b',
            r'\beduca[çc][ãa]o\s+infantil\b',
            r'\beduca[çc][ãa]o\s+b[áa]sica\b',
            r'\bacess[íi]vel\s+educa[çc][ãa]o\b',
            r'\baux[íi]lio\s+financeiro\s+educacional\b',
            r'\bseguran[çc]a\s+escolar\b',
            r'\bseguran[çc]a\s+na\s+escola\b',
            r'\bempoderamento\s+da\s+juventude\b',
            r'\bempoderamento\s+das\s+mulheres\b',
            r'\boportunidades\s+iguais\b',
            r'\btrabalho\s+infantil\b',
            r'\bdiscriminat[óo]rio\b',
            r'\blacuna\s+educacional\b',
            r'\bnecessidades\s+de\s+educa[çc][ãa]o\s+especial\b',
            r'\bsistema\s+educacional\s+inclusivo\b',
            r'\bexclus[ãa]o\s+educacional\b',
            r'\babandono\s+escolar\b',
            r'\bcidadania\s+global\b',
            r'\beduca[çc][ãa]o\s+para\s+o\s+desenvolvimento\s+sustent[áa]vel\b',
            r'\beduca[çc][ãa]o\s+ambiental\b',
            r'\bpol[íi]tica[s]?\s+educacional[es]?\b',
            r'\beduca[çc][ãa]o\s+internacional\b',
            r'\breforma\s+da\s+educa[çc][ãa]o\b',
            r'\bgovernan[çc]a\s+educacional\b',
            r'\bdespesas\s+com\s+educa[çc][ãa]o\b',
            r'\bajuda\s+externa\b',
            r'\bdesgaste\s+de\s+professores\b'
        ]

        # Expressões compostas que devem estar presentes em qualquer ordem
        termos_complexos = [
            # {ajuda ao desenvolvimento} E {treinamento de professores}
            r'(?=.*\bajuda\s+ao\s+desenvolvimento\b)(?=.*\btreinamento\s+de\s+professores\b)',

            # {oportunidades de aprendizado} E ({disparidades de gênero} OU empoderamento)
            r'(?=.*\boportunidades?\s+de\s+aprendizado\b)(?=.*\b(?:disparidades\s+de\s+g[êe]nero|empoderamento)\b)',

            # {armadilha da pobreza} E {escolaridade}
            r'(?=.*\barmadilha\s+da\s+pobreza\b)(?=.*\bescolaridade\b)',

            # {escolarização} E ({disparidades de gênero} OU {disparidades étnicas} OU {disparidades raciais})
            r'(?=.*\bescolariza[çc][ãa]o\b)(?=.*\b(?:disparidades\s+de\s+g[êe]nero|disparidades\s+[ée]tnicas|disparidades\s+raciais)\b)',

            # {reforma educacional} E {países em desenvolvimento}
            r'(?=.*\breforma\s+educacional\b)(?=.*\bpa[íi]ses\s+em\s+desenvolvimento\b)',

            # {países em desenvolvimento} E {efeitos escolares}
            r'(?=.*\bpa[íi]ses\s+em\s+desenvolvimento\b)(?=.*\befeitos\s+escolares\b)',

            # {treinamento de professores} E {países em desenvolvimento}
            r'(?=.*\btreinamento\s+de\s+professores\b)(?=.*\bpa[íi]ses\s+em\s+desenvolvimento\b)'
        ]

        # Combina termos obrigatórios com cada termo específico
        padroes = []
        for termo in termos_simples:
            padroes.append(rf"{termos_obrigatorios}.*{termo}")

        # Adiciona os padrões para expressões complexas
        padroes.extend(termos_complexos)

        return padroes

    def get_excecoes(self):
        """Define padrões de exclusão."""
        return r'\balfabetiza[çc][ãa]o\s+em\s+sa[úu]de\b'