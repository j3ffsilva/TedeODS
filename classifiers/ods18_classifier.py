from classifiers.base_classifier import BaseODSClassifier

class ODS18Classifier(BaseODSClassifier):
    def __init__(self):
        super().__init__("racial")

    def get_padroes(self):
        return [
            # Racismo e discriminação
            r'\bracismo\b',
            r'\bracismo\s+estrutural\b',
            r'\bdiscrimina[cç][aã]o\s+racial\b',
            r'\bpreconceito\s+racial\b',
            r'\bdesigualdade[s]?\s+raciais?\b',
            r'\binjusti[cç]a[s]?\s+racial[is]?\b',
            r'\bsegrega[cç][aã]o\s+racial\b',
            r'\bexclus[aã]o\s+racial\b',
            r'\bintoleran[cç]ia\s+racial\b',
            r'\bviol[eê]ncia\s+racial\b',
            r'\bcolorismo\b',
            r'\bbranqueamento\s+racial\b',

            # Grupos populacionais - composições
            r'\bpopula[cç][aã]o\s+negra\b',
            r'\bpopula[cç][aã]o\s+afrodescendente\b',
            r'\bcomunidade\s+negra\b',
            r'\bjovens?\s+negros?\b',
            r'\bmulheres?\s+negras?\b',
            r'\bhomens?\s+negros?\b',
            r'\bcrian[cç]as?\s+negras?\b',
            r'\bestudantes?\s+negros?\b',
            r'\btrabalhadores?\s+negros?\b',
            r'\bmulheres?\s+pretas?\b',
            r'\bhomens?\s+pretos?\b',

            # Afrodescendentes
            r'\bafrodescendentes?\b',
            r'\bafro[\s\-]brasileir[oa]s?\b',

            # Quilombolas
            r'\bquilombolas?\b',
            r'\bterrit[oó]rio\s+quilombola\b',
            r'\bcomunidade\s+quilombola\b',

            # Políticas e direitos
            r'\bcotas?\s+raciais?\b',
            r'\ba[cç][oõ]es?\s+afirmativas?\b',
            r'\blei\s+de\s+cotas\b',
            r'\binclus[aã]o\s+racial\b',
            r'\bequidade\s+racial\b',
            r'\bantirracismo\b',
            r'\bantirracistas?\b',
            r'\bmovimento\s+negro\b',
            r'\bconscien[cç]ia\s+negra\b',
            r'\bluta\s+antirracista\b',

            # Conceitos acadêmicos
            r'\brela[cç][oõ]es\s+raciais\b',
            r'\b[eé]tnico[\s\-]racial\b',
            r'\bdiversidade\s+racial\b',
            r'\bdiversidade\s+[eé]tnica\b',
            r'\bidentidade\s+racial\b',
            r'\bidentidade\s+negra\b',
            r'\bnegritude\b',
            r'\binterseccionalidade\b',
            r'\bdi[aá]spora\s+africana\b',
            r'\bdi[aá]spora\s+negra\b',
            r'\bcultura\s+negra\b',
            r'\bresist[eê]ncia\s+negra\b',
            r'\bvozes\s+negras\b',

            # Contexto histórico
            r'\bescraviza[cç][aã]o\b',
            r'\bp[oó]s[\s\-]aboli[cç][aã]o\b',
        ]

    def get_excecoes(self):
        return r''