from classifiers.base_classifier import BaseODSClassifier

class ODS13Classifier(BaseODSClassifier):
    def __init__(self):
        super().__init__(13)

    def get_padroes(self):
        return [
            # Termos principais
            r'(?=.*\b(?:a[çc][ãa]o\s*clim[áa]tica|clim[áa]tica\s*a[çc][ãa]o)\b)',
            r'(?=.*\b(?:adapta[çc][ãa]o\s*clim[áa]tica|clim[áa]tica\s*adapta[çc][ãa]o)\b)',
            r'(?=.*\b(?:mudan[çc]a\s*clim[áa]tica|clim[áa]tica\s*mudan[çc]a)\b)',
            r'(?=.*\bcapitalismo\s*clim[áa]tico\b)',
            r'(?=.*\bipcc\b)',
            r'(?=.*\b(?:efeito\s*clim[áa]tico|clim[áa]tico\s*efeito)\b)',
            r'(?=.*\b(?:equidade\s*clim[áa]tica|clim[áa]tica\s*equidade)\b)',
            r'(?=.*\b(?:feedback\s*clim[áa]tico|clim[áa]tico\s*feedback)\b)',
            r'(?=.*\b(?:finan[çc]as\s*clim[áa]ticas|clim[áa]ticas\s*finan[çc]as)\b)',
            r'(?=.*\b(?:financiamento\s*da\s*mudan[çc]a\s*clim[áa]tica|mudan[çc]a\s*clim[áa]tica\s*financiamento)\b)',
            r'(?=.*\b(?:imposi[çc][ãa]o\s*do\s*clima|clima\s*imposi[çc][ãa]o)\b)',
            r'(?=.*\b(?:governan[çc]a\s*clim[áa]tica|clim[áa]tica\s*governan[çc]a)\b)',
            r'(?=.*\b(?:impacto\s*clim[áa]tico|clim[áa]tico\s*impacto)\b)',
            r'(?=.*\b(?:investimento\s*clim[áa]tico|clim[áa]tico\s*investimento)\b)',
            r'(?=.*\b(?:justi[çc]a\s*clim[áa]tica|clim[áa]tica\s*justi[çc]a)\b)',
            r'(?=.*\b(?:mitiga[çc][ãa]o\s*clim[áa]tica|clim[áa]tica\s*mitiga[çc][ãa]o)\b)',
            r'(?=.*\bmodelo[s]?\s*clim[áa]tico[s]?\b)',
            r'(?=.*\b(?:modelagem\s*clim[áa]tica|clim[áa]tica\s*modelagem)\b)',
            r'(?=.*\b(?:pol[íi]tica[s]?\s*clim[áa]tica[s]?|clim[áa]tica[s]?\s*pol[íi]tica[s]?)\b)',
            r'(?=.*\b(?:risco[s]?\s*clim[áa]tico[s]?|clim[áa]tico[s]?\s*risco[s]?)\b)',
            r'(?=.*\b(?:servi[çc]o[s]?\s*clim[áa]tico[s]?|clim[áa]tico[s]?\s*servi[çc]o[s]?)\b)',
            r'(?=.*\b(?:previs[ãa]o[s]?\s*clim[áa]tica[s]?|clim[áa]tica[s]?\s*previs[ãa]o[s]?)\b)',
            r'(?=.*\b(?:sinal[s]?\s*clim[áa]tico[s]?|clim[áa]tico[s]?\s*sinal[s]?)\b)',
            r'(?=.*\b(?:ponto\s*de\s*inflex[ãa]o\s*clim[áa]tica|clim[áa]tica\s*ponto\s*de\s*inflex[ãa]o)\b)',
            r'(?=.*\b(?:varia[çc][ãa]o[s]?\s*clim[áa]tica[s]?|clim[áa]tica[s]?\s*varia[çc][ãa]o[s]?)\b)',
            r'(?=.*\becoclimatologia\b)',
            r'(?=.*\b(?:fundo\s*verde\s*(do|para\s*o)\s*clima|clima\s*fundo\s*verde)\b)',
            r'(?=.*\b(?:clima[s]?\s*regional[es]?|regional[es]?\s*clima[s]?)\b)',
            r'(?=.*\b(?:clima[s]?\s*urbano[s]?|urbano[s]?\s*clima[s]?)\b)',

            # Combinações com "clima" em qualquer ordem
            r'(?=.*\b(?:clima|gest[ãa]o\s*adaptativa)\b).*?(?=.*\b(?:clima|gest[ãa]o\s*adaptativa)\b)',
            r'(?=.*\b(?:clima|conscientiza[çc][ãa]o)\b).*?(?=.*\b(?:clima|conscientiza[çc][ãa]o)\b)',
            r'(?=.*\b(?:clima|bioeconomia)\b).*?(?=.*\b(?:clima|bioeconomia)\b)',
            r'(?=.*\b(?:clima|carbono)\b).*?(?=.*\b(?:clima|carbono)\b)',
            r'(?=.*\b(?:clima|tomada\s*de\s*decis[ãa]o)\b).*?(?=.*\b(?:clima|tomada\s*de\s*decis[ãa]o)\b)',
            r'(?=.*\b(?:clima|redu[çc][ãa]o\s*do\s*risco\s*de\s*desastres)\b).*?(?=.*\b(?:clima|redu[çc][ãa]o\s*do\s*risco\s*de\s*desastres)\b)',
            r'(?=.*\b(?:clima|educa[çc][ãa]o\s*ambiental)\b).*?(?=.*\b(?:clima|educa[çc][ãa]o\s*ambiental)\b)',
            r'(?=.*\b(?:clima|educa[çc][ãa]o\s*para\s*o\s*desenvolvimento\s*sustent[áa]vel)\b).*?(?=.*\b(?:clima|educa[çc][ãa]o\s*para\s*o\s*desenvolvimento\s*sustent[áa]vel)\b)',
            r'(?=.*\b(?:clima|conserva[çc][ãa]o\s*de\s*energia)\b).*?(?=.*\b(?:clima|conserva[çc][ãa]o\s*de\s*energia)\b)',
            r'(?=.*\b(?:clima|emiss[õo]es?)\b).*?(?=.*\b(?:clima|emiss[õo]es?)\b)',
            r'(?=.*\b(?:clima|extremo)\b).*?(?=.*\b(?:clima|extremo)\b)',
            r'(?=.*\b(?:clima|cadeia\s*alimentar)\b).*?(?=.*\b(?:clima|cadeia\s*alimentar)\b)',
            r'(?=.*\b(?:clima|perigo[s]?)\b).*?(?=.*\b(?:clima|perigo[s]?)\b)',
            r'(?=.*\b(?:clima|uso\s*da\s*terra)\b).*?(?=.*\b(?:clima|uso\s*da\s*terra)\b)',
            r'(?=.*\b(?:clima|megacidade[s]?)\b).*?(?=.*\b(?:clima|megacidade[s]?)\b)',
            r'(?=.*\b(?:clima|consumo)\b).*?(?=.*\b(?:clima|consumo)\b)',
            r'(?=.*\b(?:clima|produ[çc][ãa]o)\b).*?(?=.*\b(?:clima|produ[çc][ãa]o)\b)',
            r'(?=.*\b(?:clima|pequenas\s*ilhas\s*em\s*desenvolvimento)\b).*?(?=.*\b(?:clima|pequenas\s*ilhas\s*em\s*desenvolvimento)\b)',
            r'(?=.*\b(?:clima|antropoceno)\b).*?(?=.*\b(?:clima|antropoceno)\b)',
            r'(?=.*\b(?:clima|atmosfera[s]?)\b).*?(?=.*\b(?:clima|atmosfera[s]?)\b)',
            r'(?=.*\b(?:clima|recuo\s*das\s*geleiras)\b).*?(?=.*\b(?:clima|recuo\s*das\s*geleiras)\b)',
            r'(?=.*\b(?:clima|aquecimento)\b).*?(?=.*\b(?:clima|aquecimento)\b)',
            r'(?=.*\b(?:clima|intera[çc][ãa]o\s*gelo-oceano)\b).*?(?=.*\b(?:clima|intera[çc][ãa]o\s*gelo-oceano)\b)',
            r'(?=.*\b(?:clima|ciclo\s*do\s*nitrog[êe]nio)\b).*?(?=.*\b(?:clima|ciclo\s*do\s*nitrog[êe]nio)\b)',
            r'(?=.*\b(?:clima|acidifica[çc][ãa]o\s*dos\s*oceanos)\b).*?(?=.*\b(?:clima|acidifica[çc][ãa]o\s*dos\s*oceanos)\b)',
            r'(?=.*\b(?:clima|for[çc]ante\s*radiativa)\b).*?(?=.*\b(?:clima|for[çc]ante\s*radiativa)\b)',
            r'(?=.*\b(?:clima|gelo\s*marinho)\b).*?(?=.*\b(?:clima|gelo\s*marinho)\b)',
            r'(?=.*\b(?:clima|n[íi]vel\s*do\s*mar)\b).*?(?=.*\b(?:clima|n[íi]vel\s*do\s*mar)\b)',
            r'(?=.*\b(?:clima|expans[ãa]o\s*t[ée]rmica)\b).*?(?=.*\b(?:clima|expans[ãa]o\s*t[ée]rmica)\b)',
            r'(?=.*\b(?:clima|unfccc)\b).*?(?=.*\b(?:clima|unfccc)\b)',
            r'(?=.*\b(?:clima|oz[ôo]nio)\b).*?(?=.*\b(?:clima|oz[ôo]nio)\b)'
        ]
    
    def get_excecoes(self):
        """Define padrões de exclusão."""
        return r'\b(?:droga|geomorfologia)\b'