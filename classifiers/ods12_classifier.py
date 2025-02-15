from classifiers.base_classifier import BaseODSClassifier

class ODS12Classifier(BaseODSClassifier):
    def __init__(self):
        super().__init__(12)

    def get_padroes(self):
        return [
            r'polui[çc][ãa]o ambiental',
            r'res[íi]duos perigosos',
            r'produto[s]? qu[íi]mico[s]? perigosos?',
            r'produto[s]? qu[íi]mico[s]? t[óo]xico[s]?',
            r'polui[çc][ãa]o qu[íi]mica',
            r'destrui[çc][ãa]o do oz[ôo]nio',
            r'polui[çc][ãa]o por pesticidas',
            r'estresse de pesticidas',
            r'redu[çc][ãa]o de pesticidas',
            r'avalia[çc][ãa]o do ciclo de vida',
            r'an[áa]lise[s]? do ciclo de vida',
            r'economia de baixo carbono',
            r'pegada ambiental',
            r'pegada material',
            r'efici[êe]ncia da colheita',
            r'res[íi]duos s[óo]lidos',
            r'gera[çc][ãa]o de res[íi]duos',
            r'responsabilidade social corporativa',
            r'sustentabilidade corporativa',
            r'comportamento[s]? do consumidor',
            r'reciclagem de res[íi]duos',
            r'reciclagem de recursos',
            r'reutiliza[çc][ãa]o|reuso de recursos',
            r'economia de base biol[óo]gica',
            r'res[íi]duo zero',
            r'r[óo]tulo[s]? de sustentabilidade',
            r'extra[çc][ãa]o de recurso global',
            r'contabilidade do fluxo de materiais',
            r'metabolismo social',
            r'derramamento de (alimentos|recursos)',
            r'efici[êe]ncia de recursos',
            r'consumo sustent[áa]vel de alimentos',
            r'consumo verde',
            r'cadeia de suprimentos sustent[áa]vel',
            r'economia circular',
            r'do ber[çc]o ao ber[çc]o',
            r'compras|aquisi[çc][õo]es sustent[áa]veis',
            r'turismo sustent[áa]vel',
            r'subs[íi]dios a combust[íi]veis f[óo]sseis',
            r'gastos com combust[íi]veis f[óo]sseis',
            r'consumo.*(uso de recursos|derramamento)',
            r'produ[çc][ãa]o.*(uso de recursos|derramamento)'
        ]