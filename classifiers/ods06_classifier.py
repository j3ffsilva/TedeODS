from classifiers.base_classifier import BaseODSClassifier

class ODS06Classifier(BaseODSClassifier):
    def __init__(self):
        super().__init__(6)

    def get_padroes(self):
        return [
            # 1. Seguro e acesso à água ou água potável
            r'\bseguro.*(acesso\s*[àa]\s*[áa]gua|[áa]gua\s*pot[áa]vel)\b',

            # 2. Limpa e água potável ou fonte de água
            r'\blimpa.*([áa]gua\s*pot[áa]vel|fonte\s*de\s*[áa]gua)\b',

            # 3. Água e saneamento, qualidade ou recurso com subcondições
            r'\b[áa]gua.*?(saneamento\s*e\s*higiene|qualidade|recurso).*?(disponibilidade\s*de\s*[áa]gua|efici[êe]ncia\s*do\s*uso\s*da\s*[áa]gua|abastecimento\s*de\s*[áa]gua|[áa]gua\s*pot[áa]vel|banheiro[s]?\s*higi[êe]nico[s]?|membrana[s]?\s*anti-incrustante[s]?|gest[ãa]o\s*da\s*[áa]gua|toxicologia\s*(aqu[áa]tica|da\s*[áa]gua)|ecotoxicologia\s*(aqu[áa]tica|da\s*[áa]gua))\b',

            # 4. Água doce, qualidade e poluente/poluição/contaminação
            r'\b[áa]gua\s*(doce|fresca).*qualidade\s*da\s*[áa]gua.*(poluente|polui[çc][ãa]o|contamina.*)\b',

            # 5. Água doce e segurança hídrica ou escassez de água
            r'\b[áa]gua\s*(doce|fresca).*?\b(seguran[çc]a\s*h[íi]drica|escassez\s*de\s*[áa]gua|[áa]gua\s*residual.*?tratamento|conserva[çc][ãa]o\s*da\s*[áa]gua|pegada\s*h[íi]drica|infraestrutura\s*h[íi]drica|polui[çc][ãa]o\s*da\s*[áa]gua|purifica[çc][ãa]o\s*da\s*[áa]gua|uso[s]?\s*da\s*[áa]gua|saneamento\w*|esgoto\w*)\b',
            
            # 6. Água, ecossistema e proteção ou disruptores endócrinos
            r'\b[áa]gua.*?ecossistema.*?(prote[çc][ãa]o\s*de|disruptor(es)?\s*end[óo]crino[s]?)\b(?!.*?\bmarinhos\b)',

            # 7. Água, gestão e poluentes
            r'\b[áa]gua.*?gest[ãa]o\s*da\s*[áa]gua.*?(remedia[çc][ãa]o\s*da\s*polui[çc][ãa]o|remo[çc][ãa]o\s*de\s*poluentes)\b',

            # 8. Água subterrânea e água doce
            r'\b[áa]gua\s*subterr[âa]nea.*[áa]gua\s*doce\b',

            # 9. Poluição e água residual com tratamento
            r'\b(polui[çc][ãa]o\s*da\s*[áa]gua|poluente\s*da\s*[áa]gua).*[áa]gua\s*residual.*tratamento\b',

            # 10. Termos simples (OR)
            r'\bdisponibilidade\s*de\s*[áa]gua\s*doce\b',
            r'\bescassez\s*de\s*[áa]gua\b',
            r'\bfecalismo\s*a\s*c[ée]u\s*aberto\b',
            r'\b[áa]gua\s*azul\b',
            r'\b[áa]gua\s*verde\b',
            r'\b[áa]gua\s*cinza\b',
            r'\b[áa]gua\s*negra\b'
        ]

    def get_excecoes(self):
        """Define padrões de exclusão."""
        return r'estudo\s*da\s*carga\s*global\s*de\s*doen[çc]as\b'