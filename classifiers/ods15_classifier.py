from classifiers.base_classifier import BaseODSClassifier

class ODS15Classifier(BaseODSClassifier):
    def __init__(self):
        super().__init__(15)

    def get_padroes(self):
        return [
            # Lookahead para garantir pelo menos um termo do grupo 1 (terra, terrestre, água doce)
            
            r'(?=.*\b(?:terrestre|terra|[áa]gua\s+doce)\b)'
            # Lookahead para garantir pelo menos um termo do grupo 2 (biodiversidade, ecossistemas, conservação, etc.)
            r'(?=.*\b(?:biodivers\w*|riqueza\s+de\s+esp[ée]cies|bioeconomia\w*|produ[çc][ãa]o\s+biol[óo]gica|'
            r'desflorestamento\w*|desertif\w*|sistema\s+terrestre|resili[êe]ncia\s+ecol[óo]gica|ecossistema\w*|'
            r'cascata\s+tr[óo]fica|n[íi]vel\s+tr[óo]fico|teia\s+tr[óo]fica|esp[ée]cie[s]?\s+amea[çc]ada[s]?|'
            r'risco[s]?\s+de\s+extin[çc][ãa]o|ca[çc]a\s+(furtiva|ilegal)\w*|'
            r'produto[s]?\s+(da|de)\s+vida\s+selvagem|tr[áa]fico\s+de\s+animais\s+selvagens|'
            r'mercado[s]?\s+de\s+animais\s+selvagens|esp[ée]cie[s]?\s+(invasora[s]?|ex[óo]tica[s]?)|'
            r'uso[s]?\s+da\s+terra|degrada[çc][ãa]o\s+(do\s+solo|da\s+terra)|LULUCF|floresta\w*|'
            r'conserva[çc][ãa]o\s+do\s+solo|zona[s]?\s+[úu]mida[s]?|montanha\w*|terra\s+seca\w*|'
            r'cobertura\s+montanhosa|[áa]rea[s]?\s+protegida[s]?|REDD|manejo\s+florestal|silvicultura|'
            r'colheita\s+de\s+madeira|extra[çc][ãa]o\s+ilegal\s+de\s+madeira|corte\s+e\s+queima|'
            r'cultivo\s+de\s+pousio|cobertura\s+de\s+[áa]rvores|restaura[çc][ãa]o\s+(do\s+solo|da\s+terra|de\s+habitat)|'
            r'seca|manejo\s+sustent[áa]vel\s+da\s+terra|vegeta[çc][ãa]o\s+de\s+montanha|'
            r'esp[ée]cie[s]?\s+da\s+Lista\s+Vermelha|[íi]ndice\s+da\s+Lista\s+Vermelha|onda\s+de\s+extin[çc][ãa]o|'
            r'fragmenta[çc][ãa]o\s+de\s+habitat|perda\s+de\s+habitat|'
            r'Protocolo\s+de\s+Nagoya\s+sobre\s+Acesso\s+a\s+Recursos\s+Gen[ée]ticos|'
            r'recurso[s]?\s+gen[ée]tico[s]?|invas[ãa]o\s+biol[óo]gica|biodiversidade\s+inclusiva|'
            r'conselho\s+de\s+manejo\s+florestal|alian[çc]a\s+para\s+florestas\s+tropicais|'
            r'certifica[çc][ãa]o\s+florestal|auditoria\s+florestal|ecoturismo|'
            r'conserva[çc][ãa]o\s+baseada\s+na\s+comunidade|conflito\s+entre\s+humanos\s+e\s+animais\s+selvagens)\b)'
        ]
    
    def get_excecoes(self):
        """Define padrões de exclusão."""
        return r''