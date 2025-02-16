from classifiers.base_classifier import BaseODSClassifier

class ODS11Classifier(BaseODSClassifier):
    def __init__(self):
        super().__init__(11)

    def get_padroes(self):
        return [
            r'cidade[s]?',
            r'assentamento[s]? humano[s]?',
            r'urbano',
            r'metr[óo]pol\w*',
            r'vila\w*',
            r'municipal\w*',
            r'gentrifica[çc][ãa]o',
            r'congestionamento',
            r'transporte',
            r'transporte p[úu]blico',
            r'moradia',
            r'favela\w*',
            r'sendai framework',
            r'redu[çc][ãa]o de risco de desastres|rrd',
            r'cidade[s]? inteligente[s]?',
            r'edif[íi]cio[s]? resiliente[s]?',
            r'edif[íi]cio[s]? sustent[áa]vel[eis]?',
            r'design de edif[íi]cios',
            r'projeto de edif[íi]cios',
            r'urbaniza[çc][ãa]o',
            r'edif[íi]cio[s]? de energia zero',
            r'servi[çc]o[s]? b[áa]sico[s]?',
            r'governan[çc]a',
            r'participa[çc][ãa]o cidad[ãa]',
            r'planejamento (colaborativo|participativo)',
            r'inclus[ãa]o',
            r'patrim[ôo]nio (cultural|natural)',
            r'unesco',
            r'desastre',
            r'pegada (ecol[óo]gica|ambiental)',
            r'res[íi]duos',
            r'polui[çc][ãa]o',
            r'poluente\w*',
            r'[áa]gua residual',
            r'reciclagem',
            r'economia circular',
            r'qualidade do ar',
            r'espa[çc]o[s]? verde[s]?',
            r'que inclui a natureza',
            r'edif[íi]cio[s]?|pr[éé]dio[s]? que inclui a natureza',
            r'edif[íi]cio[s]?|pr[éé]dios inclusivos da natureza'
        ]
    
    def get_excecoes(self):
        """Define padrões de exclusão."""
        return r''