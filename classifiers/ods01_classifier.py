from classifiers.base_classifier import BaseODSClassifier

class ODS01Classifier(BaseODSClassifier):
    def __init__(self):
        super().__init__(1)

    def get_padroes(self):
        return [
            # Termos simples (OR)
            r'\bextrema\s+pobreza\b',
            r'\bal[íi]vio\s+da\s+pobreza\b',
            r'\berradica[çc][ãa]o\s+da\s+pobreza\b',
            r'\bredu[çc][ãa]o\s+da\s+pobreza\b',
            r'\blinha\s+internacional\s+de\s+pobreza\b',
            r'\bempoderamento\s+financeiro\b',
            r'\befeito[s]?\s+sobre\s+a\s+distribui[çc][ãa]o\b|\befeito[s]?\s+distributivo[s]?\b',
            r'\btrabalho\s+infantil\b',
            r'\bajuda\s+ao\s+desenvolvimento\b',
            r'\bprote[çc][ãa]o\s+social\b',
            r'\bsistema\s+de\s+prote[çc][ãa]o\s+social\b',
            r'\bmicrofinanc\w*\b',
            r'\bresili[êe]ncia\s+dos\s+pobres\b',
            r'\bbanco\s+de\s+alimentos\b',
            r'\bbancos\s+de\s+alimentos\b',

            # Relações Lógicas (AND) permitindo qualquer ordem
            r'(?=.*\bajuda\s+financeira\b)(?=.*\bpobreza\b)',
            r'(?=.*\bajuda\s+financeira\b)(?=.*\b(?:pobre|pobres)\b)',
            r'(?=.*\bajuda\s+financeira\b)(?=.*\bdivis[ãa]o\s+norte-sul\b)',
            r'(?=.*\bdesenvolvimento\s+financeiro\b)(?=.*\bpobreza\b)',
            r'(?=.*\bprote[çc][ãa]o\s+social\b)(?=.*\bacesso\b)',
            r'(?=.*\brede\s+de\s+seguran[çc]a\b)(?=.*\b(?:pobre[s]?|vulner[áa]vel[eis]*)\b)',
            r'(?=.*\brecurso\s+econ[ôo]mico\b)(?=.*\bacesso\b)',
            r'(?=.*\brecursos\s+econ[ôo]micos\b)(?=.*\bacesso\b)'
        ]
    
    def get_excecoes(self):
        """Define padrões de exclusão."""
        return r''
