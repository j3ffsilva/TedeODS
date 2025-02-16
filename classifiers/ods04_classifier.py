import re
from classifiers.base_classifier import BaseODSClassifier

class ODS04Classifier(BaseODSClassifier):
    def __init__(self):
        super().__init__(4)

    def get_padroes(self):
        """Define os padrões de busca, garantindo que um termo obrigatório coexista com um termo específico e que a substring seja capturada."""

        # Grupo de termos obrigatórios (pelo menos um deles deve estar presente)
        termos_obrigatorios = (
            r'\b(escola)\b',
            r'\b(educa[çc][ãa]o)\b',
            r'\b(educacional)\b'
        )

        # Grupo de termos específicos (pelo menos um deles deve estar presente)
        termos_especificos = (
            r'\b(frequ[êe]ncia escolar)\b',
            r'\b(matr[íi]cula escolar)\b',
            r'\b(educa[çc][ãa]o inclusiva)\b',
            r'\b(desigualdade educacional)\b',
            r'\b(qualidade educacional)\b',
            r'\b(matr[íi]cula educacional)\b',
            r'\b(alfabetiza[çc][ãa]o de adultos)\b',
            r'\b(taxa de numeramento)\b',
            r'\b(ambiente educacional)\b',
            r'\b(acesso educacional)\b',
            r'\b(ajuda ao desenvolvimento)\b.*\b(treinamento de professores)\b',
            r'\b(educa[çc][ãa]o infantil)\b',
            r'\b(educa[çc][ãa]o b[áa]sica)\b',
            r'\b(acess[íi]vel educa[çc][ãa]o)\b',
            r'\b(aux[íi]lio financeiro educacional)\b',
            r'\b(seguran[çc]a escolar)\b',
            r'\b(seguran[çc]a na escola)\b',
            r'\b(oportunidades? de aprendizado)\b.*\b(disparidades de g[êe]nero|empoderamento)\b',
            r'\b(empoderamento da juventude)\b',
            r'\b(empoderamento das mulheres)\b',
            r'\b(oportunidades iguais)\b',
            r'\b(trabalho infantil)\b',
            r'\b(discriminat[óo]rio)\b',
            r'\b(lacuna educacional)\b',
            r'\b(armadilha da pobreza)\b.*\b(escolaridade)\b',
            r'\b(necessidades de educa[çc][ãa]o especial)\b',
            r'\b(sistema educacional inclusivo)\b',
            r'\b(escolariza[çc][ãa]o)\b.*\b(disparidades de g[êe]nero|disparidades [ée]tnicas|disparidades raciais)\b',
            r'\b(exclus[ãa]o educacional)\b',
            r'\b(abandono escolar)\b',
            r'\b(cidadania global)\b',
            r'\b(educa[çc][ãa]o para o desenvolvimento sustent[áa]vel)\b',
            r'\b(educa[çc][ãa]o ambiental)\b',
            r'\b(pol[ií]tica[s]? educacional[es]?)\b',
            r'\b(educa[çc][ãa]o internacional)\b',
            r'\b(reforma da educa[çc][ãa]o)\b',
            r'\b(reforma educacional)\b.*\b(pa[ií]ses em desenvolvimento)\b',
            r'\b(governan[çc]a educacional)\b',
            r'\b(pa[ií]ses em desenvolvimento)\b.*\b(efeitos escolares)\b',
            r'\b(despesas com educa[çc][ãa]o)\b',
            r'\b(ajuda externa)\b',
            r'\b(treinamento de professores)\b.*\b(pa[ií]ses em desenvolvimento)\b',
            r'\b(desgaste de professores)\b'
        )

        # Criação da regex única garantindo co-ocorrência e captura das substrings encontradas
        return [rf'(?=.*(?:{"|".join(termos_obrigatorios)}))'
                rf'(?=.*(?:{"|".join(termos_especificos)}))'
                rf'(?P<match>(?:{"|".join(termos_especificos)}))']

    def get_excecoes(self):
        """Define padrões de exclusão."""
        return r'\b(alfabetiza[çc][ãa]o em sa[úu]de)\b'