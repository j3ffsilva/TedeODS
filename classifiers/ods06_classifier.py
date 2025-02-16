from classifiers.base_classifier import BaseODSClassifier

class ODS06Classifier(BaseODSClassifier):
    def __init__(self):
        super().__init__(6)

    def get_padroes(self):
        return [
            r'seguro.*(acesso [àa] [áa]gua|[áa]gua pot[áa]vel)',
            r'limpa.*([áa]gua pot[áa]vel|fonte de [áa]gua)',
            r'[áa]gua.*(saneamento e higiene|qualidade|recurso)',
            r'[áa]gua.*(disponibilidade de [áa]gua|efici[êe]ncia do uso da [áa]gua|abastecimento de [áa]gua)',
            r'[áa]gua.*(banheiro higi[êe]nico|banheiros higi[êe]nicos)',
            r'[áa]gua.*(membrana anti-incrustante|membranas anti-incrustantes)',
            r'[áa]gua.*gest[ãa]o da [áa]gua',
            r'[áa]gua.*(toxicologia aqu[áa]tica|toxicologia da [áa]gua)',
            r'[áa]gua.*(ecotoxicologia aqu[áa]tica|ecotoxicologia da [áa]gua)',
            r'[áa]gua doce.*qualidade da [áa]gua.*(poluente|polui[çc][ãa]o|contamina\w*)',
            r'[áa]gua doce.*(seguran[çc]a h[íi]drica|escassez de [áa]gua)',
            r'[áa]gua residual.*tratamento',
            r'conserva[çc][ãa]o da [áa]gua',
            r'pegada h[íi]drica',
            r'infraestrutura h[íi]drica',
            r'polui[çc][ãa]o da [áa]gua',
            r'purifica[çc][ãa]o da [áa]gua',
            r'uso[s]? da [áa]gua',
            r'saneamento\w*',
            r'esgoto\w*',
            r'[áa]gua.*ecossistema.*(prote[çc][ãa]o de|disruptor end[óo]crino|disruptores end[óo]crinos)',
            r'[áa]gua.*gest[ãa]o da [áa]gua.*(remedia[çc][ãa]o da polui[çc][ãa]o|remo[çc][ãa]o de poluentes)',
            r'[áa]gua subterr[âa]nea.*[áa]gua doce',
            r'(polui[çc][ãa]o da [áa]gua|poluente da [áa]gua).*([áa]gua residual.*tratamento)',
            r'disponibilidade de [áa]gua doce',
            r'escassez de [áa]gua',
            r'fecalismo a c[ée]u aberto',
            r'[áa]gua azul',
            r'[áa]gua verde',
            r'[áa]gua cinza',
            r'[áa]gua negra'
        ]
    
    def get_excecoes(self):
        """Define padrões de exclusão."""
        return r''