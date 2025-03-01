from classifiers.base_classifier import BaseODSClassifier

class ODS03Classifier(BaseODSClassifier):
    def __init__(self):
        super().__init__(3)

    def get_padroes(self):
        return [
            # {humano} E ({saúde*} OU {doença*} OU {remédio*} OU {mortalidade})
            r'(?=.*\bhumano\b)(?=.*\b(?:sa[úu]de\w*|doen[çc]a\w*|rem[ée]dio\w*|mortalidade)\b)',

            # Termos isolados
            r'\bs[íi]ndrome\s+da\s+crian[çc]a\s+espancada\b',
            r'\bdoen[çc]a[s]?\s+cardiovascular[es]?\b',
            r'\bchagas\b',
            r'\babuso\s+infantil\b',
            r'\bneglig[êe]ncia\s+infantil\b',
            r'\b[íi]ndice\s+de\s+bem-estar\s+(infantil|juvenil)\b',
            r'\bdoen[çc]a[s]?\s+transmitida[s]?\s+pela\s+[áa]gua\b',
            r'\bdoen[çc]a[s]?\s+tropical[es]?\b',
            r'\bdoen[çc]a[s]?\s+respirat[óo]ria[s]?\s+cr[ôo]nica[s]?\b',
            r'\bdoen[çc]a[s]?\s+infecciosa[s]?\b',
            r'\bdoen[çc]a[s]?\s+sexualmente\s+transmiss[ií]vel[eis]?\b',
            r'\bdoen[çc]a[s]?\s+transmiss[ií]vel[eis]?\b',
            r'\bsida\b|\baids\b|\bhiv\b|\bv[ií]rus\s+da\s+imunodefici[êe]ncia\s+humana\b',
            r'\btuberculose\b',
            r'\bmal[áa]ria\b',
            r'\bhepatite\b',
            r'\bpoliomielite\w*\b',
            r'\bvacina\w*\b',
            r'\bc[âa]ncer\w*\b',
            r'\bdiabetes\w*\b',
            r'\bmortalidade\s+(materna|infantil|neonatal|prematura)\b',
            r'\bcomplica[çc][õo]es\s+no\s+parto\b',
            r'\bano\s+de\s+vida\s+ajustado\s+pela\s+qualidade\b',
            r'\bsa[úu]de\s+materna\b',
            r'\bmorte[s]?\s+evit[áa]vel[eis]?\b',
            r'\bcontrole\s+do\s+tabaco\b',
            r'\babuso\s+de\s+(subst[âa]ncias|drogas)\b',
            r'\buso\s+de\s+(tabaco|[áa]lcool)\b',
            r'\bdepend[êe]ncia\s+de\s+(subst[âa]ncias|qu[ií]mica|drogas)\b',
            r'\btabagismo\b|\balcoolismo\b',
            r'\bsuic[ií]dio\w*\b',
            r'\bdepress[ãa]o\s+p[óo]s-parto\b',
            r'\b(zika\s+v[ií]rus|dengue|esquistossomose|doen[çc]a\s+do\s+sono|ebola)\b',
            r'\bsa[úu]de\s+mental\b',
            r'\btranstorno[s]?\s+mental[es]?\b',
            r'\bdoen[çc]a[s]?\s+mental[es]?\b',
            r'\bsarampo\b',
            r'\bdoen[çc]a[s]?\s+negligenciada[s]?\b',
            r'\b(diarreia|c[óo]lera|disenteria|febre\s+tifoide)\b',
            r'\bacidente[s]?\s+de\s+tr[âa]nsito\b',
            r'\bestilo\s+de\s+vida\s+saud[áa]vel\b',
            r'\bexpectativa[s]?\s+de\s+vida\b',
            r'\bpol[íi]tica\s+de\s+sa[úu]de\b',

            # {sistema de saúde} E (acesso OU acessível)
            r'(?=.*\bsistema\s+de\s+sa[úu]de\b)(?=.*\b(?:acesso|acess[ií]vel)\b)',

            # Outros termos isolados
            r'\brisco[s]?\s+de\s+sa[úu]de\b',
            r'\bsa[úu]de\s+inclusiva\b',
            r'\bobesidade\b',
            r'\bdeterminantes\s+sociais\s+de\s+sa[úu]de\b',
            r'\bdano\s+psicol[óo]gico\b',
            r'\bbem-estar\s+psicol[óo]gico\b',
            r'\bsa[úu]de\s+p[úu]blica\b'
        ]

    def get_excecoes(self):
        """Define padrões de exclusão."""
        return r''