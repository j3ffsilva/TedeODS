from classifiers.base_classifier import BaseODSClassifier

class ODS08Classifier(BaseODSClassifier):
    def __init__(self):
        super().__init__(8)

    def get_padroes(self):
        return [
            # Expressões fixas (sem lookaheads)
            r'\bcrescimento\s+econ[ôo]mico\b',
            r'\bpol[íi]tica\s+de\s+desenvolvimento\s+econ[ôo]mico\b',
            r'\bpol[íi]tica\s+de\s+emprego\b',
            r'\bcrescimento\s+econ[ôo]mico\s+inclusivo\b',
            r'\bcrescimento\s+sustent[áa]vel\b',
            r'\bdesenvolvimento\s+econ[ôo]mico\b',
            r'\bglobaliza[çc][ãa]o\s+econ[ôo]mica\b',
            r'\bprodutividade\s+econ[ôo]mica\b',
            r'\beconomia\s+de\s+baixo\s+carbono\b',
            r'\bcrescimento\s+inclusivo\b',
            r'\bmicrocr[ée]dito\w*\b',
            r'\brenda\s+igual\b',
            r'\bsal[áa]rios\s+iguais\b',
            r'\bemprego[s]?\s+decente[s]?\b',
            r'\bemprego[s]?\s+de\s+qualidade\b',
            r'\bcria[çc][ãa]o\s+de\s+emprego\b',
            r'\bpleno\s+emprego\b',
            r'\bprote[çc][ãa]o\s+do\s+emprego\b',
            r'\bemprego[s]?\s+informal[es]?\b',
            r'\bemprego[s]?\s+prec[áa]rio[s]?\b',
            r'\bdesemprego\b',
            r'\btrabalho[s]?\s+prec[áa]rio[s]?\b',
            r'\bmicroempresa\w*\b',
            r'\bpequena\s+empresa\b',
            r'\bm[ée]dia\s+empresa\b',
            r'\bpequenas\s+empresas\b',
            r'\bm[ée]dias\s+empresas\b',
            r'\bpequeno[s]?\s+empres[áa]rio[s]?\b',
            r'\bempres[áa]rio[s]?\s+iniciante[s]?\b',
            r'\bm[ée]dio[s]?\s+empres[áa]rio[s]?\b',
            r'\bpequeno[s]?\s+empreendedor[es]?\b',
            r'\bm[ée]dio[s]?\s+empreendedor[es]?\b',
            r'\bempreendedor[es]?\s+iniciante[s]?\b',
            r'\bempreendedorismo\s+social\b',
            r'\bambiente\s+de\s+trabalho\s+seguro\b',
            r'\binstitui[çc][ãa]o\s+do\s+mercado\s+de\s+trabalho\b',
            r'\binstitui[çc][õo]es\s+do\s+mercado\s+de\s+trabalho\b',
            r'\btrabalho\s+for[çc]ado\b',
            r'\btrabalho\s+infantil\b',
            r'\bdireito[s]?\s+trabalhista[s]?\b',
            r'\bescravid[ãa]o\s+moderna\b',
            r'\btr[áa]fico\s+de\s+pessoas\b',
            r'\bcrianc[aã]-soldado\b',
            r'\bcrian[çc]as-soldado\b',
            r'\bemprego[s]?\s+global[es]?\b',
            r'\bsal[áa]rio\s+m[íi]nimo\b',
            r'\beconomia\s+circular\b',
            r'\beconomia\s+inclusiva\b',
            r'\beconomia\s+rural\b',
            r'\binvestimento\s+de\s+desenvolvimento\s+estrangeiro\b',
            r'\bajuda\s+ao\s+com[ée]rcio\b',
            r'\bsindicatos?\b',
            r'\btrabalhadores\s+pobres\b',
            r'\bn[ãa]o\s+est[áa]\s+em\s+educa[çc][ãa]o,\s+emprego\s+ou\s+treinamento\b',
            r'\bcompensa[çc][ãa]o\s+de\s+carbono\b',
            r'\bprojeto[s]?\s+de\s+compensa[çc][ãa]o\b',
            r'\bdiversifica[çc][ãa]o\s+econ[ôo]mica\b',
            r'\bpegada\s+material\b',
            r'\befici[êe]ncia\s+de\s+recursos\b',
            r'\bdissocia[çc][ãa]o\s+econ[ôo]mica\b',
            r'\bdisparidades\s+do\s+mercado\s+de\s+trabalho\b',
            r'\bturismo\s+sustent[áa]vel\b',
            r'\becoturismo\b',
            r'\bturismo\s+baseado\s+na\s+comunidade\b',
            r'\bemprego\s+no\s+turismo\b',
            r'\bpol[íi]tica\s+de\s+turismo\s+sustent[áa]vel\b',
            r'\bacesso\s+financeiro\b',
            r'\binclus[ãa]o\s+financeira\b',
            r'\bacesso\s+a\s+servi[çc]os\s+banc[áa]rios\b',

            # Expressões que exigem presença de múltiplos termos (com lookaheads)
            r'(?=.*\bber[çc]o\s+ao\s+ber[çc]o\b)(?=.*\beconomia\b)'
        ]
    
    def get_excecoes(self):
        """Define padrões de exclusão."""
        return r'\bsa[úu]de\b'