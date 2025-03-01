from classifiers.base_classifier import BaseODSClassifier

class ODS14Classifier(BaseODSClassifier):
    def __init__(self):
        super().__init__(14)

    def get_padroes(self):
        return [
            # Lookahead para garantir pelo menos um termo do grupo 1 (mar, oceano, costa, etc.)
            r'(?=.*\b(?:marinho|oceano[s]?|mar[es]?|costa\w*|mangue)\b)'
            # Lookahead para garantir pelo menos um termo do grupo 2 (processos oceânicos, conservação, pesca, etc.)
            r'(?=.*\b(?:ciclo[s]?\s+da\s+[áa]gua|ciclo[s]?\s+biogeoqu[íi]mico[s]?|'
            r'modelo[s]?\s+de\s+circula[çc][ãa]o\s+oce[âa]nica|'
            r'modelagem\s+de\s+circula[çc][ãa]o\s+oce[âa]nica|'
            r'iceocean|oceano\s+gelado|eutr[óo]fica\w*|marinha|branqueamento\s+de\s+corais|'
            r'manejo|gest[ãa]o\s+costeir[oa]|habitat[s]?\s+costeir[oa]s?|'
            r'lixo\s+marinho|acidifica[çc][ãa]o\s+dos\s+oceanos|'
            r'acidifica[çc][ãa]o.*[áa]gua\s+do\s+mar|pesca|pesca\s+excessiva|'
            r'rendimento\s+sustent[áa]vel|[áa]rea[s]?\s+marinha[s]?\s+protegida[s]?|'
            r'conserva[çc][ãa]o\s+marinha|ecoturismo|conserva[çc][ãa]o\s+baseada\s+na\s+comunidade|'
            r'deslizamento\s+de\s+terra\s+marinha|polui[çc][ãa]o\s+marinha|'
            r'escoamento\s+de\s+nutrientes|ecoturismo\s+costeiro|'
            r'pesca\s+destrutiva|pesca\s+local|pescadores\s+artesanais|'
            r'direitos\s+de\s+pesca|riqueza\s+de\s+esp[ée]cies|'
            r'conhecimento\s+ecol[óo]gico\s+tradicional|pequenas\s+ilhas\s+em\s+desenvolvimento|'
            r'cota\s+marinha|economia\s+marinha|pol[íi]tica\s+marinha)\b)'
        ]
    
    def get_excecoes(self):
        """Define padrões de exclusão."""
        return r'\b(?:paleoclima|paleoceanografia|radiocarbono|gen[ée]tica|medicina|droga|engenharia|aerossol)\b'
