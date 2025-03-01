from classifiers.base_classifier import BaseODSClassifier

class ODS10Classifier(BaseODSClassifier):
    def __init__(self):
        super().__init__(10)

    def get_padroes(self):
        return [
            # Frases fixas
            r'\b(?:igualdade|desigualdade)\s+(?:econ[ôo]mica|financeira|socioecon[ôo]mica)\b',
            r'\bpol[íi]tica[s]?\s+de\s+reforma\s+econ[ôo]mica\b',
            r'\binclus[ãa]o\s+pol[íi]tica\b',
            r'\bpol[íi]tica[s]?\s+de\s+prote[çc][ãa]o\s+social\b',
            r'\binvestimento\s+estrangeiro\s+direto\b',
            r'\blacuna[s]?\s+de\s+desenvolvimento\b',
            r'\bremessa\s+de\s+migrantes\b',
            r'\bmigra[çc][ãa]o\s+respons[áa]vel\b',
            r'\bpol[íi]tica[s]?\s+de\s+migra[çc][ãa]o|migrat[óo]ria[s]?\b',
            r'\bdivis[ãa]o\s+norte-sul\b',
            r'\bexclus[ãa]o\s+social\b',
            r'\bmarginaliza[çc][ãa]o\s+econ[ôo]mica\b',
            r'\bdesigualdade\s+de\s+renda\b',
            r'\blei[s]?\s+discriminat[óo]ria[s]?\b',
            r'\bpol[íi]tica[s]?\s+discriminat[óo]ria[s]?\b',
            r'\bempoderamento\s+econ[ôo]mico\b',
            r'\btransforma[çc][ãa]o\s+econ[ôo]mica\b',

            # Migração e exclusões (imigração/emigração sem relação com química, doença ou biodiversidade)
            r'(?=.*\b(?:imigra[çc][ãa]o|emigra[çc][ãa]o)\b)(?!.*\b(?:qu[íi]mica|doen[çc]a|biodiversidade)\b)',

            # Desenvolvimento + tarifas ou isenção de impostos
            r'(?=.*\bdesenvolvimento\b)(?=.*\b(?:tarifas?|tarifa\s+zero|acesso\s+isento\s+de\s+impostos)\b)',

            # Mercado global + empoderamento (qualquer ordem)
            r'(?=.*\bmercado\s+global\b)(?=.*\bempoderamento\b)'
        ]
    
    def get_excecoes(self):
        """Define padrões de exclusão."""
        return r''