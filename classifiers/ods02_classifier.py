from classifiers.base_classifier import BaseODSClassifier

class ODS02Classifier(BaseODSClassifier):
    def __init__(self):
        super().__init__(2)

    def get_padroes(self):
        return [
            # Termos simples
            r'\bdireitos\s*de\s*posse\s*da\s*terra\b',
            r'\bdesnutri[çc][ãa]o\b',
            r'\bdesnutrid[oa]\b',
            r'\bsubnutri[çc][ãa]o\b',
            r'\bsubnutrid[oa]\b',
            r'\bprodu[çc][ãa]o\s*agr[íi]cola\b',
            r'\bprodutividade\s*agr[íi]cola\b',
            r'\bpr[áa]ticas\s*agr[íi]colas\b',
            r'\bmanejo\s*agr[íi]cola\b|\bgest[ãa]o\s*agr[íi]cola\b',
            r'\bprodu[çc][ãa]o\s*alimentar\b|\bprodu[çc][ãa]o\s*de\s*alimentos\b',
            r'\bprodutividade\s*alimentar\b|\bprodutividade\s*de\s*alimentos\b',
            r'\bseguran[çc]a\s*alimentar\b',
            r'\binseguran[çc]a\s*alimentar\b',
            r'\bdireito[s]?\s*[àa]\s*terra\b',
            r'\breforma\s*agr[áa]ria\b',
            r'\breformas\s*agr[áa]rias\b',
            r'\bpr[áa]ticas\s*agr[íi]colas\s*resilientes\b',
            r'\bfome\s*oculta\b',
            r'\balimentos\s*geneticamente\s*modificados\b',
            r'\bpr[áa]ticas\s*agroflorestais\b',
            r'\bmanejo\s*agroflorestal\b|\bgest[ãa]o\s*agroflorestal\b',
            r'\binova[çc][ãa]o\s*agr[íi]cola\b',
            r'\bgovernan[çc]a\s*alimentar\b',
            r'\bcadeia\s*de\s*abastecimento\s*alimentar\b',
            r'\bcadeia\s*de\s*valor\s*alimentar\b',
            r'\bmercado\s*de\s*commodities\s*alimentares\b',

            # Combinações com "E" (permitindo qualquer ordem)
            r'(?=.*\bpequeno\s*produtor\b)(?=.*\b(?:fazenda|silvicultura|pastoril|agricultura|pesca|produtor\s*de\s*alimentos|produtores\s*de\s*alimentos)\b)',
            r'(?=.*\bagricultura\b)(?=.*\bpot[áa]ssio\b)',
            r'(?=.*\btransg[êe]nicos\b)(?=.*\balimentos\b)',
            r'(?=.*\bseguran[çc]a\s*alimentar\b)(?=.*\bdiversidade\s*gen[ée]tica\b)',
            r'(?=.*\bmercado\s*de\s*alimentos\b)(?=.*\b(?:restri[çc][ãa]o|tarifa|acesso|divis[ãa]o\s*norte-sul|governan[çc]a\s*do\s*desenvolvimento)\b)',

            # Fertilizante e nutrição alimentar
            r'\bmelhoria\s*da\s*nutri[çc][ãa]o\s*alimentar\b',
            r'\bfertilizante\b'
        ]

    def get_excecoes(self):
        """Exclui textos relacionados a doenças."""
        return r'\bdoen[çc]a[s]?\b'