from classifiers.base_classifier import BaseODSClassifier

class ODS13Classifier(BaseODSClassifier):
    def __init__(self):
        super().__init__(13)

    def get_padroes(self):
        return [
            r'a[çc][ãa]o clim[áa]tica',
            r'adapta[çc][ãa]o clim[áa]tica',
            r'mudan[çc]a clim[áa]tica',
            r'capitalismo clim[áa]tico',
            r'ipcc',
            r'efeito clim[áa]tico',
            r'equidade clim[áa]tica',
            r'feedback clim[áa]tico',
            r'finan[çc]as clim[áa]ticas',
            r'financiamento da mudan[çc]a clim[áa]tica',
            r'imposi[çc][ãa]o do clima',
            r'governan[çc]a clim[áa]tica',
            r'impacto clim[áa]tico',
            r'investimento clim[áa]tico',
            r'justi[çc]a clim[áa]tica',
            r'mitiga[çc][ãa]o clim[áa]tica',
            r'modelo[s]? clim[áa]tico[s]?',
            r'modelagem clim[áa]tica',
            r'pol[íi]tica[s]? clim[áa]tica[s]?',
            r'risco[s]? clim[áa]tico[s]?',
            r'servi[çc]os? clim[áa]tico[s]?',
            r'previs[ãa]o clim[áa]tica|previs[õo]es clim[áa]ticas',
            r'sinal[s]? clim[áa]tico[s]?',
            r'ponto de inflex[ãa]o clim[áa]tica',
            r'varia[çc][ãa]o[s]? clim[áa]tica[s]?',
            r'ecoclimatologia',
            r'fundo verde do clima|fundo verde para o clima',
            r'clima[s]? regional[es]?',
            r'clima[s]? urbano[s]?',
            r'clima.*(gest[ãa]o adaptativa|conscientiza[çc][ãa]o|bioeconomia|carbono|tomada de decis[ãa]o|redu[çc][ãa]o do risco de desastres|educa[çc][ãa]o ambiental|educa[çc][ãa]o para o desenvolvimento sustent[áa]vel|conserva[çc][ãa]o de energia|emiss[õo]es?|extremo|cadeia alimentar|cadeias alimentares|estrutura|perigo[s]?|ilha[s]?|uso da terra|megacidade[s]?|consumo|produ[çc][ãa]o|pequenas ilhas em desenvolvimento|antropoceno|atmosfera[s]?|mecanismo de desenvolvimento limpo|recuo das geleiras|aquecimento|estufa|intera[çc][ãa]o gelo-oceano|intera[çc][õo]es gelo-oceano|ciclo do nitrog[êe]nio|ciclos do nitrog[êe]nio|acidifica[çc][ãa]o dos oceanos|for[çc]ante radiativa|gelo marinho|n[íi]vel do mar|n[íi]veis do mar|expans[ãa]o t[ée]rmica|unfccc|oz[ôo]nio)'
        ]
    
    def get_excecoes(self):
        """Define padrões de exclusão."""
        return r''