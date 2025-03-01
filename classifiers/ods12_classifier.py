from classifiers.base_classifier import BaseODSClassifier

class ODS12Classifier(BaseODSClassifier):
    def __init__(self):
        super().__init__(12)

    def get_padroes(self):
        return [
            r'\bpolui[çc][ãa]o\s+ambiental\b',
            r'\bres[íi]duos\s+perigosos\b',
            r'\bproduto\s+qu[íi]mico\s+perigoso\b',
            r'\bprodutos\s+qu[íi]micos\s+perigosos\b',
            r'\bproduto\s+qu[íi]mico\s+t[óo]xico\b',
            r'\bprodutos\s+qu[íi]micos\s+t[óo]xicos\b',
            r'\bpolui[çc][ãa]o\s+qu[íi]mica\b',
            r'\bdesttrui[çc][ãa]o\s+do\s+oz[ôo]nio\b',
            r'\bpolui[çc][ãa]o\s+por\s+pesticidas\b',
            r'\bestresse\s+de\s+pesticidas\b',
            r'\bredu[çc][ãa]o\s+de\s+pesticidas\b',
            r'\bavalia[çc][ãa]o\s+do\s+ciclo\s+de\s+vida\b',
            r'\ban[áa]lise[s]?\s+do\s+ciclo\s+de\s+vida\b',
            r'\beconomia\s+de\s+baixo\s+carbono\b',
            r'\bpegada\s+ambiental\b',
            r'\bpegada\s+material\b',
            r'\befici[êe]ncia\s+da\s+colheita\b',
            r'\bres[íi]duos\s+s[óo]lidos\b',
            r'\bgera[çc][ãa]o\s+de\s+res[íi]duos\b',
            r'\bresponsabilidade\s+social\s+corporativa\b',
            r'\bsustentabilidade\s+corporativa\b',
            r'\bcomportamento[s]?\s+do\s+consumidor\b',
            r'\breciclagem\s+de\s+res[íi]duos\b',
            r'\breciclagem\s+de\s+recursos\b',
            r'\breutiliza[çc][ãa]o|reuso\s+de\s+recursos\b',
            r'\beconomia\s+de\s+base\s+biol[óo]gica\b',
            r'\bres[íi]duo\s+zero\b',
            r'\br[óo]tulo\s+de\s+sustentabilidade\b',
            r'\brotulagem\s+de\s+sustentabilidade\b',
            r'\bextra[çc][ãa]o\s+de\s+recurso\s+global\b',
            r'\bcontabilidade\s+do\s+fluxo\s+de\s+materiais\b',
            r'\bmetabolismo\s+social\b',
            r'\bderramamento\s+de\s+alimentos\b',
            r'\bderramamento\s+de\s+recursos\b',
            r'\befici[êe]ncia\s+de\s+recursos\b',
            r'\bconsumo\s+sustent[áa]vel\s+de\s+alimentos\b',
            r'\bconsumo\s+verde\b',
            r'\bcadeia\s+de\s+suprimentos\s+sustent[áa]vel\b',
            r'\beconomia\s+circular\b',
            r'\bdo\s+ber[çc]o\s+ao\s+ber[çc]o\b',
            r'\b(compras|aquisi[çc][õo]es)\s+sustent[áa]veis\b',
            r'\bturismo\s+sustent[áa]vel\b',
            r'\bsubs[íi]dios\s+a\s+combust[íi]veis\s+f[óo]sseis\b',
            r'\bgastos\s+com\s+combust[íi]veis\s+f[óo]sseis\b',

            # Expressões compostas com OR dentro da expressão
            r'(?=.*\bconsumo\b)(?=.*\b(uso\s+de\s+recursos|derramamento)\b)',
            r'(?=.*\bprodu[çc][ãa]o\b)(?=.*\b(uso\s+de\s+recursos|derramamento)\b)'
        ]
    
    def get_excecoes(self):
        """Define padrões de exclusão."""
        return r'\b(?:rede[s]? (de )?sensores sem fio|rede sem fio|sem fio|doen[çc]a|astrof[íi]sica)\b'