from classifiers.base_classifier import BaseODSClassifier

class ODS11Classifier(BaseODSClassifier):
    def __init__(self):
        super().__init__(11)

    def get_padroes(self):
        return [
            r'(?=.*\b(?:cidade[s]?|assentamento[s]?\s+humano[s]?|urbano|metr[óo]pol\w*|vila\w*|municipal\w*)\b)'
            r'(?=.*\b(?:gentrifica[çc][ãa]o|congestionamento|transporte(?:\s+p[úu]blico)?|moradia|favela\w*|'
            r'sendai\s+framework|redu[çc][ãa]o\s+de\s+risco\s+de\s+desastres|rrd|'
            r'cidade[s]?\s+inteligente[s]?|edif[íi]cio[s]?\s+(?:resiliente[s]?|sustent[áa]vel[eis]?)|'
            r'design\s+de\s+edif[íi]cios|projeto\s+de\s+edif[íi]cios|urbaniza[çc][ãa]o|'
            r'edif[íi]cio[s]?\s+de\s+energia\s+zero|servi[çc]o[s]?\s+b[áa]sico[s]?|governan[çc]a|'
            r'participa[çc][ãa]o\s+cidad[ãa]|planejamento\s+(?:colaborativo|participativo)|inclus[ãa]o|'
            r'patrim[ôo]nio\s+(?:cultural|natural)|unesco|desastre|pegada\s+(?:ecol[óo]gica|ambiental)|'
            r'res[íi]duos|polui[çc][ãa]o|poluente\w*|[áa]gua\s+residual|reciclagem|'
            r'economia\s+circular|qualidade\s+do\s+ar|espa[çc]o[s]?\s+verde[s]?|'
            r'que\s+inclui\s+a\s+natureza|(?:edif[íi]cio[s]?|pr[ée]dio[s]?)\s+que\s+inclui\s+a\s+natureza|'
            r'(?:edif[íi]cio[s]?|pr[ée]dio[s]?)\s+inclusivo[s]?\s+da\s+natureza)\b)'
        ]

    def get_excecoes(self):
        """Define padrões de exclusão."""
        return r''