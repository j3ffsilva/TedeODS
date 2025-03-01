from classifiers.base_classifier import BaseODSClassifier

class ODS07Classifier(BaseODSClassifier):
    def __init__(self):
        super().__init__(7)

    def get_padroes(self):
        return [
            # Expressões fixas (sem lookaheads)
            r'\befici[êe]ncia\s+energ[ée]tica\b',
            r'\bconsumo\s+de\s+energia\b',
            r'\btransi[çc][ãa]o\s+energ[ée]tica\b',
            r'\btecnologia\s+de\s+energia\s+limpa\b',
            r'\bequidade\s+energ[ée]tica\b',
            r'\bjusti[çc]a\s+energ[ée]tica\b',
            r'\bpobreza\s+energ[ée]tica\b',
            r'\bpol[íi]tica\s+energ[ée]tica\b',
            r'\brenov[áa]vel\w*\b',
            r'\bsociedade\s+de\s+2000\s+watts\b',
            r'\bmicro-rede\s+inteligente\b',
            r'\brede\s+inteligente\b',
            r'\bmicrorrede\s+inteligente\b',
            r'\bmicro-redes\s+inteligentes\b',
            r'\bredes\s+inteligentes\b',
            r'\bmicrorredes\s+inteligentes\b',
            r'\bmedidor\s+inteligente\b',
            r'\bmedidores\s+inteligentes\b',
            r'\beletricidade\s+acess[íi]vel\b',
            r'\bconsumo\s+de\s+eletricidade\b',
            r'\beletricidade\s+confi[áa]vel\b',
            r'\bcombust[íi]vel\s+limpo\b',
            r'\bcombust[íi]vel\s+limpo\s+para\s+cozinhar\b',
            r'\bpobreza\s+de\s+combust[íi]vel\b',
            r'\benergiewende\b',
            r'\bavalia[çc][ãa]o\s+do\s+ciclo\s+de\s+vida\b',
            r'\bavalia[çc][õo]es\s+do\s+ciclo\s+de\s+vida\b',
            r'\bfotovoltaica\b',
            r'\bdivis[ãa]o\s+fotocatal[íi]tica\s+da\s+[áa]gua\b',
            r'\bprodu[çc][ãa]o\s+de\s+hidrog[êe]nio\b',
            r'\bdivis[ãa]o\s+da\s+[áa]gua\b',
            r'\bbateria[s]?\s+de\s+[íi]on-l[íi]tio\b',
            r'\brede\s+de\s+calor\b',
            r'\bcalor\s+distrital\b',
            r'\baquecimento\s+distrital\b',
            r'\bconsumo\s+de\s+energia\s+(residencial|dom[ée]stica)\b',
            r'\bseguran[çc]a\s+energ[ée]tica\b',
            r'\beletrifica[çc][ãa]o\s+rural\b',
            r'\bescada\s+de\s+energia\b',
            r'\bacesso\s+[àa]\s+energia\b',
            r'\bconserva[çc][ãa]o\s+de\s+energia\b',
            r'\bsociedade\s+de\s+baixo\s+carbono\b',
            r'\bsistema[s]?\s+h[íi]brido[s]?\s+de\s+energia\s+renov[áa]vel\b',
            r'\btroca\s+de\s+combust[íi]vel\b',
            r'\bgovernan[çc]a\s+energ[ée]tica\b',

            # Expressões que exigem presença de múltiplos termos (com lookaheads)
            r'(?=.*\bfotoqu[íi]mica\b)(?=.*\benergia\s+renov[áa]vel\b)',
            r'(?=.*\bajuda\s+externa\s+(ao|para\s+o)\s+desenvolvimento\b)(?=.*\benergia\s+renov[áa]vel\b)',
            r'(?=.*\bassist[êe]ncia\s+oficial\s+ao\s+desenvolvimento\b)(?=.*\beletricidade\b)',
            r'(?=.*\bdesenvolvimento\s+energ[ée]tico\b)(?=.*\bpa[ií]ses\s+em\s+desenvolvimento\b)',
        ]
    
    def get_excecoes(self):
        """Define padrões de exclusão."""
        return r'\brede[s]?\s+de\s+sensores\s+sem\s+fio\b'
