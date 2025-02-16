from classifiers.base_classifier import BaseODSClassifier

class ODS09Classifier(BaseODSClassifier):
    def __init__(self):
        super().__init__(9)

    def get_padroes(self):
        return [
            r'crescimento industrial',
            r'diversifica[çc][ãa]o industrial',
            r'desenvolvimento de infraestrutura',
            r'investimento em infraestrutura',
            r'infraestrutura p[úu]blica',
            r'infraestrutura resiliente',
            r'infraestrutura transfronteiri[çc]a',
            r'infraestruturas p[úu]blicas',
            r'infraestruturas resilientes',
            r'infraestruturas transfronteiri[çc]as',
            r'emiss[õo]es industriais.*mitiga[çc][ãa]o',
            r'gest[ãa]o de res[íi]duos industriais',
            r'tratamento de res[íi]duos industriais',
            r'congestionamento de tr[áa]fego',
            r'microempresa\w*',
            r'pequena empresa',
            r'm[ée]dia empresa',
            r'pequenas empresas',
            r'm[ée]dias empresas',
            r'pequeno[s]? empres[áa]rio[s]?',
            r'm[ée]dio[s]? empres[áa]rio[s]?',
            r'pequeno[s]? empreendedor[es]?',
            r'm[ée]dio[s]? empreendedor[es]?',
            r'gest[ãa]o da cadeia de valor',
            r'acesso [àa] banda larga.*pa[íi]ses em desenvolvimento',
            r'inova[çc][ãa]o em manufatura',
            r'investimento em manufatura',
            r'transporte sustent[áa]vel',
            r'transporte acess[íi]vel',
            r'servi[çc]os de transporte',
            r'transporte inclusivo',
            r'investimento em P&D',
            r'produto[s]? verde[s]?',
            r'manufatura sustent[áa]vel',
            r'ber[çc]o ao ber[çc]o.*ind[úu]stria',
            r'cadeia de suprimentos de circuito fechado',
            r'inova[çc][ãa]o.*industrial',
            r'inova[çc][ãa]o de processo',
            r'inova[çc][ãa]o de produto',
            r'inova[çc][ãa]o inclusiva'
        ]
    
    def get_excecoes(self):
        """Define padrões de exclusão."""
        return r''