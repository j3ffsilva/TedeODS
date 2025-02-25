from classifiers.base_classifier import BaseODSClassifier

class ODS09Classifier(BaseODSClassifier):
    def __init__(self):
        super().__init__(9)

    def get_padroes(self):
        return [
            r'crescimento\s*industrial',
            r'diversifica[çc][ãa]o\s*industrial',
            r'desenvolvimento\s*de\s*infraestrutura',
            r'investimento\s*em\s*infraestrutura',
            r'infraestrutura\s*p[úu]blica',
            r'infraestrutura\s*resiliente',
            r'infraestrutura\s*transfronteiri[çc]a',
            r'infraestruturas\s*p[úu]blicas',
            r'infraestruturas\s*resilientes',
            r'infraestruturas\s*transfronteiri[çc]as',
            r'emiss[õo]es\s*industriais.*mitiga[çc][ãa]o',
            r'gest[ãa]o\s*de\s*res[íi]duos\s*industriais',
            r'tratamento\s*de\s*res[íi]duos\s*industriais',
            r'congestionamento\s*de\s*tr[áa]fego',
            r'microempresa\w*',
            r'pequena\s*empresa',
            r'm[ée]dia\s*empresa',
            r'pequenas\s*empresas',
            r'm[ée]dias\s*empresas',
            r'pequeno[s]?\s*empres[áa]rio[s]?',
            r'm[ée]dio[s]?\s*empres[áa]rio[s]?',
            r'pequeno[s]?\s*empreendedor[es]?',
            r'm[ée]dio[s]?\s*empreendedor[es]?',
            r'gest[ãa]o\s*da\s*cadeia\s*de\s*valor',
            r'acesso\s*[àa]\s*banda\s*larga.*pa[íi]ses\s*em\s*desenvolvimento',
            r'inova[çc][ãa]o\s*em\s*manufatura',
            r'investimento\s*em\s*manufatura',
            r'transporte\s*sustent[áa]vel',
            r'transporte\s*acess[íi]vel',
            r'servi[çc]os\s*de\s*transporte',
            r'transporte\s*inclusivo',
            r'investimento\s*em\s*P&D',
            r'produto[s]?\s*verde[s]?',
            r'manufatura\s*sustent[áa]vel',
            r'ber[çc]o\s*ao\s*ber[çc]o.*ind[úu]stria',
            r'cadeia\s*de\s*suprimentos\s*de\s*circuito\s*fechado',
            r'inova[çc][ãa]o.*industrial',
            r'inova[çc][ãa]o\s*de\s*processo',
            r'inova[çc][ãa]o\s*de\s*produto',
            r'inova[çc][ãa]o\s*inclusiva'
        ]
    
    def get_excecoes(self):
        """Define padrões de exclusão."""
        return r''