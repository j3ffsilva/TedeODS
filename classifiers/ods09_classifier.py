from classifiers.base_classifier import BaseODSClassifier

class ODS09Classifier(BaseODSClassifier):
    def __init__(self):
        super().__init__(9)

    def get_padroes(self):
        return [
            # Expressões fixas (sem lookaheads)
            r'\bcrescimento\s+industrial\b',
            r'\bdiversifica[çc][ãa]o\s+industrial\b',
            r'\bdesenvolvimento\s+de\s+infraestrutura\b',
            r'\binvestimento\s+em\s+infraestrutura\b',
            r'\binfraestrutura\s+p[úu]blica\b',
            r'\binfraestrutura\s+resiliente\b',
            r'\binfraestrutura\s+transfronteiri[çc]a\b',
            r'\binfraestruturas\s+p[úu]blicas\b',
            r'\binfraestruturas\s+resilientes\b',
            r'\binfraestruturas\s+transfronteiri[çc]as\b',
            r'\bgest[ãa]o\s+de\s+res[íi]duos\s+industriais\b',
            r'\btratamento\s+de\s+res[íi]duos\s+industriais\b',
            r'\bcongestionamento\s+de\s+tr[áa]fego\b',
            r'\bmicroempresa\w*\b',
            r'\bpequena\s+empresa\b',
            r'\bm[ée]dia\s+empresa\b',
            r'\bpequenas\s+empresas\b',
            r'\bm[ée]dias\s+empresas\b',
            r'\bpequeno[s]?\s+empres[áa]rio[s]?\b',
            r'\bm[ée]dio[s]?\s+empres[áa]rio[s]?\b',
            r'\bpequeno[s]?\s+empreendedor[es]?\b',
            r'\bm[ée]dio[s]?\s+empreendedor[es]?\b',
            r'\bgest[ãa]o\s+da\s+cadeia\s+de\s+valor\b',
            r'\binova[çc][ãa]o\s+em\s+manufatura\b',
            r'\binvestimento\s+em\s+manufatura\b',
            r'\btransporte\s+sustent[áa]vel\b',
            r'\btransporte\s+acess[íi]vel\b',
            r'\bservi[çc]os\s+de\s+transporte\b',
            r'\btransporte\s+inclusivo\b',
            r'\binvestimento\s+em\s+P&D\b',
            r'\bproduto[s]?\s+verde[s]?\b',
            r'\bmanufatura\s+sustent[áa]vel\b',
            r'\bcadeia\s+de\s+suprimentos\s+de\s+circuito\s+fechado\b',
            r'\binova[çc][ãa]o\s+de\s+processo\b',
            r'\binova[çc][ãa]o\s+de\s+produto\b',
            r'\binova[çc][ãa]o\s+inclusiva\b',

            # Expressões que exigem presença de múltiplos termos (com lookaheads)
            r'(?=.*\bemiss[õo]es\s+industriais\b)(?=.*\bmitiga[çc][ãa]o\b)',
            r'(?=.*\bacesso\s+[àa]\s+banda\s+larga\b)(?=.*\bpa[íi]ses\s+em\s+desenvolvimento\b)',
            r'(?=.*\bber[çc]o\s+ao\s+ber[çc]o\b)(?=.*\bind[úu]stria\b)',
            r'(?=.*\binova[çc][ãa]o\b)(?=.*\bindustrial\b)'
        ]
    
    def get_excecoes(self):
        """Define padrões de exclusão."""
        return r''