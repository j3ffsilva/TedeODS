from classifiers.base_classifier import BaseODSClassifier

class ODS10Classifier(BaseODSClassifier):
    def __init__(self):
        super().__init__(10)

    def get_padroes(self):
        return [
            r'igualdade.*(econ[ôo]mica|financeira|socioecon[ôo]mica)',
            r'desigualdade.*(econ[ôo]mica|financeira|socioecon[ôo]mica)',
            r'pol[íi]tica[s]?\s*de\s*reforma\s*econ[ôo]mica',
            r'inclus[ãa]o\s*pol[íi]tica',
            r'pol[íi]tica[s]?\s*de\s*prote[çc][ãa]o\s*social',
            r'imigra[çc][ãa]o(?!.*(qu[íi]mica|doen[çc]a|biodiversidade))',
            r'emigra[çc][ãa]o(?!.*(qu[íi]mica|doen[çc]a|biodiversidade))',
            r'investimento\s*estrangeiro\s*direto',
            r'lacuna[s]?\s*de\s*desenvolvimento',
            r'remessa\s*de\s*migrantes',
            r'migra[çc][ãa]o\s*respons[áa]vel',
            r'pol[íi]tica[s]?\s*de\s*migra[çc][ãa]o|migrat[óo]ria[s]?',
            r'divis[ãa]o\s*norte-sul',
            r'desenvolvimento.*(tarifas?|tarifa\s*zero|acesso\s*isento\s*de\s*impostos)',
            r'exclus[ãa]o\s*social',
            r'marginaliza[çc][ãa]o\s*econ[ôo]mica',
            r'desigualdade\s*de\s*renda',
            r'lei[s]?\s*discriminat[óo]ria[s]?',
            r'pol[íi]tica[s]?\s*discriminat[óo]ria[s]?',
            r'empoderamento\s*econ[ôo]mico',
            r'transforma[çc][ãa]o\s*econ[ôo]mica',
            r'mercado\s*global.*empoderamento'
        ]
    
    def get_excecoes(self):
        """Define padrões de exclusão."""
        return r''    