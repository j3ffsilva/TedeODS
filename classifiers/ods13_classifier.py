from classifiers.base_classifier import BaseODSClassifier

class ODS13Classifier(BaseODSClassifier):
    def __init__(self):
        super().__init__(13)

    def get_padroes(self):
        return [
            # Expressões fixas (mantêm a ordem original)
            r'\ba[çc][ãa]o\s*clim[áa]tica\b',
            r'\badapta[çc][ãa]o\s*clim[áa]tica\b',
            r'\bmudan[çc]a\s*clim[áa]tica\b',
            r'\bcapitalismo\s*clim[áa]tico\b',
            r'\bipcc\b',
            r'\befeito\s*clim[áa]tico\b',
            r'\bequidade\s*clim[áa]tica\b',
            r'\bfeedback\s*clim[áa]tico\b',
            r'\bfinan[çc]as\s*clim[áa]ticas\b',
            r'\bfinanciamento\s*da\s*mudan[çc]a\s*clim[áa]tica\b',
            r'\bimposi[çc][ãa]o\s*do\s*clima\b',
            r'\bgovernan[çc]a\s*clim[áa]tica\b',
            r'\bimpacto\s*clim[áa]tico\b',
            r'\binvestimento\s*clim[áa]tico\b',
            r'\bjusti[çc]a\s*clim[áa]tica\b',
            r'\bmitiga[çc][ãa]o\s*clim[áa]tica\b',
            r'\bmodelo[s]?\s*clim[áa]tico[s]?\b',
            r'\bmodelagem\s*clim[áa]tica\b',
            r'\bpol[íi]tica[s]?\s*clim[áa]tica[s]?\b',
            r'\brisco[s]?\s*clim[áa]tico[s]?\b',
            r'\bservi[çc]o[s]?\s*clim[áa]tico[s]?\b',
            r'\bprevis[ãa]o[s]?\s*clim[áa]tica[s]?\b',
            r'\bsinal[s]?\s*clim[áa]tico[s]?\b',
            r'\bponto\s*de\s*inflex[ãa]o\s*clim[áa]tica\b',
            r'\bvaria[çc][ãa]o[s]?\s*clim[áa]tica[s]?\b',
            r'\becoclimatologia\b',
            r'\bfundo\s*verde\s*(?:do|para\s*o)\s*clima\b',
            r'\bclima[s]?\s*regional[es]?\b',
            r'\bclima[s]?\s*urbano[s]?\b',

            # Combinações complexas (usam lookaheads para garantir que os termos estejam presentes em qualquer ordem)
            r'(?=.*\bclima\b)(?=.*\bgest[ãa]o\s*adaptativa\b)',
            r'(?=.*\bclima\b)(?=.*\bconscientiza[çc][ãa]o\b)',
            r'(?=.*\bclima\b)(?=.*\bbioeconomia\b)',
            r'(?=.*\bclima\b)(?=.*\bcarbono\b)',
            r'(?=.*\bclima\b)(?=.*\btomada\s*de\s*decis[ãa]o\b)',
            r'(?=.*\bclima\b)(?=.*\bredu[çc][ãa]o\s*do\s*risco\s*de\s*desastres\b)',
            r'(?=.*\bclima\b)(?=.*\beduca[çc][ãa]o\s*ambiental\b)',
            r'(?=.*\bclima\b)(?=.*\beduca[çc][ãa]o\s*para\s*o\s*desenvolvimento\s*sustent[áa]vel\b)',
            r'(?=.*\bclima\b)(?=.*\bconserva[çc][ãa]o\s*de\s*energia\b)',
            r'(?=.*\bclima\b)(?=.*\bemiss[õo]es?\b)',
            r'(?=.*\bclima\b)(?=.*\bextremo\b)',
            r'(?=.*\bclima\b)(?=.*\bcadeia[s]?\s*alimentar[es]?\b)',
            r'(?=.*\bclima\b)(?=.*\bestrutura\b)',
            r'(?=.*\bclima\b)(?=.*\bperigo[s]?\b)',
            r'(?=.*\bclima\b)(?=.*\bilha[s]?\b)',
            r'(?=.*\bclima\b)(?=.*\buso\s*da\s*terra\b)',
            r'(?=.*\bclima\b)(?=.*\bmegacidade[s]?\b)',
            r'(?=.*\bclima\b)(?=.*\bconsumo\b)',
            r'(?=.*\bclima\b)(?=.*\bprodu[çc][ãa]o\b)',
            r'(?=.*\bclima\b)(?=.*\bpequenas\s*ilhas\s*em\s*desenvolvimento\b)',
            r'(?=.*\bclima\b)(?=.*\bantropoceno\b)',
            r'(?=.*\bclima\b)(?=.*\batmosfera[s]?\b)',
            r'(?=.*\bclima\b)(?=.*\bmecanismo\s*de\s*desenvolvimento\s*limpo\b)',
            r'(?=.*\bclima\b)(?=.*\brecuo\s*das\s*geleiras\b)',
            r'(?=.*\bclima\b)(?=.*\baquecimento\b)',
            r'(?=.*\bclima\b)(?=.*\bestufa\b)',
            r'(?=.*\bclima\b)(?=.*\bintera[çc][ãa]o[s]?\s*gelo-oceano\b)',
            r'(?=.*\bclima\b)(?=.*\bciclo[s]?\s*do\s*nitrog[êe]nio\b)',
            r'(?=.*\bclima\b)(?=.*\bacidifica[çc][ãa]o\s*dos\s*oceanos\b)',
            r'(?=.*\bclima\b)(?=.*\bfor[çc]ante\s*radiativa\b)',
            r'(?=.*\bclima\b)(?=.*\bgelo\s*marinho\b)',
            r'(?=.*\bclima\b)(?=.*\bn[íi]vel\s*do\s*mar[s]?\b)',
            r'(?=.*\bclima\b)(?=.*\bexpans[ãa]o\s*t[ée]rmica\b)',
            r'(?=.*\bclima\b)(?=.*\bunfccc\b)',
            r'(?=.*\bclima\b)(?=.*\boz[ôo]nio\b)',
        ]
    
    def get_excecoes(self):
        """Define padrões de exclusão."""
        return r'\b(?:droga|geomorfologia)\b'