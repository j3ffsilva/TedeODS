from classifiers.base_classifier import BaseODSClassifier

class ODS13Classifier(BaseODSClassifier):
    def __init__(self):
        super().__init__(13)

    def get_padroes(self):
        return [
            # Termos principais
            r'a[çc][ãa]o\s*clim[áa]tica',
            r'adapta[çc][ãa]o\s*clim[áa]tica',
            r'mudan[çc]a\s*clim[áa]tica',
            r'capitalismo\s*clim[áa]tico',
            r'ipcc',
            r'efeito\s*clim[áa]tico',
            r'equidade\s*clim[áa]tica',
            r'feedback\s*clim[áa]tico',
            r'finan[çc]as\s*clim[áa]ticas',
            r'financiamento\s*da\s*mudan[çc]a\s*clim[áa]tica',
            r'imposi[çc][ãa]o\s*do\s*clima',
            r'governan[çc]a\s*clim[áa]tica',
            r'impacto\s*clim[áa]tico',
            r'investimento\s*clim[áa]tico',
            r'justi[çc]a\s*clim[áa]tica',
            r'mitiga[çc][ãa]o\s*clim[áa]tica',
            r'modelo[s]?\s*clim[áa]tico[s]?',
            r'modelagem\s*clim[áa]tica',
            r'pol[íi]tica[s]?\s*clim[áa]tica[s]?',
            r'risco[s]?\s*clim[áa]tico[s]?',
            r'servi[çc]o[s]?\s*clim[áa]tico[s]?',
            r'previs[ãa]o[s]?\s*clim[áa]tica[s]?',
            r'sinal[s]?\s*clim[áa]tico[s]?',
            r'ponto\s*de\s*inflex[ãa]o\s*clim[áa]tica',
            r'varia[çc][ãa]o[s]?\s*clim[áa]tica[s]?',
            r'ecoclimatologia',
            r'fundo\s*verde\s*(do|para\s*o)\s*clima',
            r'clima[s]?\s*regional[es]?',
            r'clima[s]?\s*urbano[s]?',

            # Combinações com "clima"
            r'clima.*?(?:gest[ãa]o\s*adaptativa|conscientiza[çc][ãa]o|bioeconomia|carbono|tomada\s*de\s*decis[ãa]o|redu[çc][ãa]o\s*do\s*risco\s*de\s*desastres|educa[çc][ãa]o\s*ambiental|educa[çc][ãa]o\s*para\s*o\s*desenvolvimento\s*sustent[áa]vel|conserva[çc][ãa]o\s*de\s*energia|emiss[õo]es?|extremo|cadeia\s*alimentar|cadeias\s*alimentares|estrutura|perigo[s]?|ilha[s]?|uso\s*da\s*terra|megacidade[s]?|consumo|produ[çc][ãa]o|pequenas\s*ilhas\s*em\s*desenvolvimento|antropoceno|atmosfera[s]?|mecanismo\s*de\s*desenvolvimento\s*limpo|recuo\s*das\s*geleiras|aquecimento|estufa|intera[çc][ãa]o\s*gelo-oceano|intera[çc][õo]es\s*gelo-oceano|ciclo\s*do\s*nitrog[êe]nio|ciclos\s*do\s*nitrog[êe]nio|acidifica[çc][ãa]o\s*dos\s*oceanos|for[çc]ante\s*radiativa|gelo\s*marinho|n[íi]vel\s*do\s*mar|n[íi]veis\s*do\s*mar|expans[ãa]o\s*t[ée]rmica|unfccc|oz[ôo]nio)'
        ]
    
    def get_excecoes(self):
        """Define padrões de exclusão."""
        return r'\b(?:droga|geomorfologia)\b'