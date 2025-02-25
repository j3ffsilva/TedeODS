from classifiers.base_classifier import BaseODSClassifier

class ODS12Classifier(BaseODSClassifier):
    def __init__(self):
        super().__init__(12)

    def get_padroes(self):
        return [
            r'polui[çc][ãa]o\s*ambiental',
            r'res[íi]duos\s*perigosos',
            r'produto[s]?\s*qu[íi]mico[s]?\s*perigosos?',
            r'produto[s]?\s*qu[íi]mico[s]?\s*t[óo]xico[s]?',
            r'polui[çc][ãa]o\s*qu[íi]mica',
            r'destrui[çc][ãa]o\s*do\s*oz[ôo]nio',
            r'polui[çc][ãa]o\s*por\s*pesticidas',
            r'estresse\s*de\s*pesticidas',
            r'redu[çc][ãa]o\s*de\s*pesticidas',
            r'avalia[çc][ãa]o\s*do\s*ciclo\s*de\s*vida',
            r'an[áa]lise[s]?\s*do\s*ciclo\s*de\s*vida',
            r'economia\s*de\s*baixo\s*carbono',
            r'pegada\s*ambiental',
            r'pegada\s*material',
            r'efici[êe]ncia\s*da\s*colheita',
            r'res[íi]duos\s*s[óo]lidos',
            r'gera[çc][ãa]o\s*de\s*res[íi]duos',
            r'responsabilidade\s*social\s*corporativa',
            r'sustentabilidade\s*corporativa',
            r'comportamento[s]?\s*do\s*consumidor',
            r'reciclagem\s*de\s*res[íi]duos',
            r'reciclagem\s*de\s*recursos',
            r'reutiliza[çc][ãa]o|reuso\s*de\s*recursos',
            r'economia\s*de\s*base\s*biol[óo]gica',
            r'res[íi]duo\s*zero',
            r'r[óo]tulo[s]?\s*de\s*sustentabilidade',
            r'extra[çc][ãa]o\s*de\s*recurso\s*global',
            r'contabilidade\s*do\s*fluxo\s*de\s*materiais',
            r'metabolismo\s*social',
            r'derramamento\s*de\s*(alimentos|recursos)',
            r'efici[êe]ncia\s*de\s*recursos',
            r'consumo\s*sustent[áa]vel\s*de\s*alimentos',
            r'consumo\s*verde',
            r'cadeia\s*de\s*suprimentos\s*sustent[áa]vel',
            r'economia\s*circular',
            r'do\s*ber[çc]o\s*ao\s*ber[çc]o',
            r'compras|aquisi[çc][õo]es\s*sustent[áa]veis',
            r'turismo\s*sustent[áa]vel',
            r'subs[íi]dios\s*a\s*combust[íi]veis\s*f[óo]sseis',
            r'gastos\s*com\s*combust[íi]veis\s*f[óo]sseis',
            r'consumo.*(uso\s*de\s*recursos|derramamento)',
            r'produ[çc][ãa]o.*(uso\s*de\s*recursos|derramamento)'
        ]
    
    def get_excecoes(self):
        """Define padrões de exclusão."""
        return r'\b(?:rede[s]? (de )?sensores sem fio|sem fio|doen[çc]a|astrof[íi]sica)\b'