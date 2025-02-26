from classifiers.base_classifier import BaseODSClassifier

class ODS15Classifier(BaseODSClassifier):
    def __init__(self):
        super().__init__(15)

    def get_padroes(self):
        return [
            # Termos primários
            r'(?=.*\bterrestre\b)',
            r'(?=.*\bterra\b)',
            r'(?=.*\b[áa]gua\s*doce\b)',

            # Combinações específicas
            r'(?=.*\bbiodivers\w*\b)',
            r'(?=.*\briqueza\s*de\s*esp[ée]cies\b)',
            r'(?=.*\bbioeconomia\w*\b)',
            r'(?=.*\bprodu[çc][ãa]o\s*biol[óo]gica\b)',
            r'(?=.*\bdesflorestamento\w*\b)',
            r'(?=.*\bdesertif\w*\b)',
            r'(?=.*\bsistema\s*terrestre\b)',
            r'(?=.*\bresili[êe]ncia\s*ecol[óo]gica\b)',
            r'(?=.*\becossistema\w*\b)',
            r'(?=.*\bcascata\s*tr[óo]fica\b)',
            r'(?=.*\bn[íi]vel\s*tr[óo]fico\b)',
            r'(?=.*\bteia\s*tr[óo]fica\b)',
            r'(?=.*\besp[ée]cie[s]?\s*amea[çc]ada[s]?\b)',
            r'(?=.*\brisco[s]?\s*de\s*extin[çc][ãa]o\b)',
            r'(?=.*\bca[çc]a\s*(furtiva|ilegal)\w*\b)',
            r'(?=.*\bproduto[s]?\s*(da|de)\s*vida\s*selvagem\b)',
            r'(?=.*\btr[áa]fico\s*de\s*animais\s*selvagens\b)',
            r'(?=.*\bmercado[s]?\s*de\s*animais\s*selvagens\b)',
            r'(?=.*\besp[ée]cie[s]?\s*(invasora[s]?|ex[óo]tica[s]?)\b)',
            r'(?=.*\buso[s]?\s*da\s*terra\b)',
            r'(?=.*\bdegrada[çc][ãa]o\s*(do\s*solo|da\s*terra)\b)',
            r'(?=.*\bLULUCF\b)',
            r'(?=.*\bfloresta\w*\b)',
            r'(?=.*\bconserva[çc][ãa]o\s*do\s*solo\b)',
            r'(?=.*\bzona[s]?\s*[úu]mida[s]?\b)',
            r'(?=.*\bmontanha\w*\b)',
            r'(?=.*\bterra\s*seca\w*\b)',
            r'(?=.*\bcobertura\s*montanhosa\b)',
            r'(?=.*\b[áa]rea[s]?\s*protegida[s]?\b)',
            r'(?=.*\bREDD\b)',
            r'(?=.*\bmanejo\s*florestal\b)',
            r'(?=.*\bsilvicultura\b)',
            r'(?=.*\bcolheita\s*de\s*madeira\b)',
            r'(?=.*\bextra[çc][ãa]o\s*ilegal\s*de\s*madeira\b)',
            r'(?=.*\bcorte\s*e\s*queima\b)',
            r'(?=.*\bcultivo\s*de\s*pousio\b)',
            r'(?=.*\bcobertura\s*de\s*[áa]rvores\b)',
            r'(?=.*\brestaura[çc][ãa]o\s*(do\s*solo|da\s*terra|de\s*habitat)\b)',
            r'(?=.*\bseca\b)',
            r'(?=.*\bmanejo\s*sustent[áa]vel\s*da\s*terra\b)',
            r'(?=.*\bvegeta[çc][ãa]o\s*de\s*montanha\b)',
            r'(?=.*\besp[ée]cie[s]?\s*da\s*Lista\s*Vermelha\b)',
            r'(?=.*\b[íi]ndice\s*da\s*Lista\s*Vermelha\b)',
            r'(?=.*\bonda\s*de\s*extin[çc][ãa]o\b)',
            r'(?=.*\bfragmenta[çc][ãa]o\s*de\s*habitat\b)',
            r'(?=.*\bperda\s*de\s*habitat\b)',
            r'(?=.*\bProtocolo\s*de\s*Nagoya\s*sobre\s*Acesso\s*a\s*Recursos\s*Gen[ée]ticos\b)',
            r'(?=.*\brecurso[s]?\s*gen[ée]tico[s]?\b)',
            r'(?=.*\binvas[ãa]o\s*biol[óo]gica\b)',
            r'(?=.*\bbiodiversidade\s*inclusiva\b)',
            r'(?=.*\bconselho\s*de\s*manejo\s*florestal\b)',
            r'(?=.*\balian[çc]a\s*para\s*florestas\s*tropicais\b)',
            r'(?=.*\bcertifica[çc][ãa]o\s*florestal\b)',
            r'(?=.*\bauditoria\s*florestal\b)',
            r'(?=.*\becoturismo\b)',
            r'(?=.*\bconserva[çc][ãa]o\s*baseada\s*na\s*comunidade\b)',
            r'(?=.*\bconflito\s*entre\s*humanos\s*e\s*animais\s*selvagens\b)'
        ]
    
    def get_excecoes(self):
        """Define padrões de exclusão."""
        return r''