from classifiers.base_classifier import BaseODSClassifier

class ODS14Classifier(BaseODSClassifier):
    def __init__(self):
        super().__init__(14)

    def get_padroes(self):
        return [
            # Termos primários
            r'(?=.*\bmarinho\b)',
            r'(?=.*\boceano[s]?\b)',
            r'(?=.*\bmar[es]?\b)',
            r'(?=.*\bcosta\w*\b)',
            r'(?=.*\bmangue\b)',

            # Combinações específicas
            r'(?=.*\bciclo[s]?\s*da\s*[áa]gua\b)',
            r'(?=.*\bciclo[s]?\s*biogeoqu[íi]mico[s]?\b)',
            r'(?=.*\bmodelo[s]?\s*de\s*circula[çc][ãa]o\s*oce[âa]nica\b)',
            r'(?=.*\bmodelagem\s*de\s*circula[çc][ãa]o\s*oce[âa]nica\b)',
            r'(?=.*\biceocean|oceano\s*gelado\b)',
            r'(?=.*\beutr[óo]fica\w*\b)',
            r'(?=.*\bmarinha\b)',
            r'(?=.*\bbranqueamento\s*de\s*corais\b)',
            r'(?=.*\bmanejo|gest[ãa]o\s*costeir[oa]\b)',
            r'(?=.*\bhabitat[s]?\s*costeir[oa]s?\b)',
            r'(?=.*\blixo\s*marinho\b)',
            r'(?=.*\bacidifica[çc][ãa]o\s*dos\s*oceanos\b)',
            r'(?=.*\bacidifica[çc][ãa]o.*[áa]gua\s*do\s*mar\b)',

            # Pesca e conservação
            r'(?=.*\bpesca\b)',
            r'(?=.*\bpesca\s*excessiva\b)',
            r'(?=.*\brendimento\s*sustent[áa]vel\b)',
            r'(?=.*\b[áa]rea[s]?\s*marinha[s]?\s*protegida[s]?\b)',
            r'(?=.*\bconserva[çc][ãa]o\s*marinha\b)',
            r'(?=.*\becoturismo\b)',
            r'(?=.*\bconserva[çc][ãa]o\s*baseada\s*na\s*comunidade\b)',
            r'(?=.*\bdeslizamento\s*de\s*terra\s*marinha\b)',
            r'(?=.*\bpolui[çc][ãa]o\s*marinha\b)',
            r'(?=.*\bescoamento\s*de\s*nutrientes\b)',
            r'(?=.*\becoturismo\s*costeiro\b)',

            # Pesca e direitos
            r'(?=.*\bpesca\s*destrutiva\b)',
            r'(?=.*\bpesca\s*local\b)',
            r'(?=.*\bpescadores\s*artesanais\b)',
            r'(?=.*\bdireitos\s*de\s*pesca\b)',
            r'(?=.*\briqueza\s*de\s*esp[ée]cies\b)',
            r'(?=.*\bconhecimento\s*ecol[óo]gico\s*tradicional\b)',
            r'(?=.*\bpequenas\s*ilhas\s*em\s*desenvolvimento\b)',
            r'(?=.*\bcota\s*marinha\b)',
            r'(?=.*\beconomia\s*marinha\b)',
            r'(?=.*\bpol[íi]tica\s*marinha\b)'
        ]
    
    def get_excecoes(self):
        """Define padrões de exclusão."""
        return r'\b(?:paleoclima|paleoceanografia|radiocarbono|gen[ée]tica|medicina|droga|engenharia|aerossol)\b'