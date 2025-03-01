from classifiers.base_classifier import BaseODSClassifier

class ODS05Classifier(BaseODSClassifier):
    def __init__(self):
        super().__init__(5)

    def get_padroes(self):
        return [
            # Termos fixos da busca original
            r'\bdesigualdade\s+de\s+g[êe]nero\b',
            r'\bigualdade\s+de\s+g[êe]nero\b',
            r'\bigualdade\s+no\s+emprego\b',
            r'\bdiferen[çc]a\s+salarial\s+entre\s+g[êe]neros\b',
            r'\bparticipa[çc][ãa]o\s+feminina\s+na\s+for[çc]a\s+de\s+trabalho\b',
            r'\bparticipa[çc][ãa]o\s+da[s]?\s+mulher[es]?\s+na\s+for[çc]a\s+de\s+trabalho\b',
            r'\bemprego\s+feminino\b',
            r'\bdesemprego\s+feminino\b',
            r'\bcasamento[s]?\s+for[çc]ado[s]?\b',
            r'\bcasamento[s]?\s+infantil[es]?\b',
            r'\bsegrega[çc][ãa]o\s+ocupacional\b',
            r'\bempoderamento\s+de\s+mulheres\b',
            r'\bempoderamento\s+de\s+meninas\b',
            r'\bempoderamento\s+feminino\b',
            r'\bmutila[çc][ãa]o\s+genital\s+feminina\b',
            r'\bcorte\s+genital\s+feminino\b',
            r'\bviol[êe]ncia\s+dom[ée]stica\b',
            r'\bviol[êe]ncia\s+sexual\b',
            r'\bparticipa[çc][ãa]o\s+pol[íi]tica\s+das\s+mulheres\b',
            r'\bparticipa[çc][ãa]o\s+pol[íi]tica\s+feminina\b',
            r'\bgestoras\s+femininas\b',
            r'\bmulheres\s+na\s+lideran[çc]a\b',
            r'\blideran[çc]a\s+feminina\b',
            r'\baloca[çc][ãa]o\s+intrafamiliar\b',
            r'\bassassinato[s]?\s+de\s+honra\b',
            r'\banti-mulheres\b',
            r'\bfeminismo\b',
            r'\bmisoginia\b',
            r'\binfantic[íi]dio[s]?\s+feminino[s]?\b',
            r'\btr[áa]fico\s+humano\b',
            r'\bprostitui[çc][ãa]o\s+for[çc]ada\b',
            r'\bdireitos\s+das\s+mulheres\b',
            r'\binjusti[çc]a[s]?\s+de\s+g[êe]nero\b',
            r'\bdiscrimina[çc][ãa]o\s+de\s+g[êe]nero\b',
            r'\bdisparidades\s+de\s+g[êe]nero\b',
            r'\bdiferen[çc]a\s+de\s+g[êe]nero\b',
            r'\bexplora[çc][ãa]o\s+feminina\b',
            r'\bequidade\s+dom[ée]stica\b',
            r'\bsub-representa[çc][ãa]o\s+das\s+mulheres\b',
            r'\bempreendedorismo\s+feminino\b',
            r'\bpropriedade\s+feminina\b',
            r'\bdesenvolvimento\s+econ[ôo]mico\s+das\s+mulheres\b',
            r'\bpoder\s+das\s+mulheres\b',
            r'\bor[çc]amento\s+sens[íi]vel\s+ao\s+g[êe]nero\b',
            r'\bcota\s+de\s+g[êe]nero\b',
            r'\bsegrega[çc][ãa]o\s+de\s+g[êe]nero\b',
            r'\bviol[êe]ncia\s+de\s+g[êe]nero\b',
            r'\bparticipa[çc][ãa]o\s+de\s+g[êe]nero\b',
            r'\bmulheres\s+na\s+pol[íi]tica\b',
            r'\bcomportamento\s+contraceptivo\b',
            r'\bautonomia\s+das\s+mulheres\b',
            r'\bfeminismo\s+agr[áa]rio\b',
            r'\bmicrocr[ée]dito\b',
            r'\bsubsist[êe]ncia\s+das\s+mulheres\b',
            r'\bpropriedade\s+das\s+mulheres\b',
            r'\bpequena\s+propriet[áa]ria\b',
            r'\btransversaliza[çc][ãa]o\s+de\s+g[êe]nero\b',

            # Expressões com "E" (qualquer ordem)
            r'(?=.*\btrabalho\s+n[ãa]o\s+remunerado\b)(?=.*\bdesigualdade\s+de\s+g[êe]nero\b)',
            r'(?=.*\btrabalho\s+de\s+cuidado\s+n[ãa]o\s+remunerado\b)(?=.*\bdesigualdade\s+de\s+g[êe]nero\b)',
            r'(?=.*\bigualdade\b)(?=.*\b(direitos\s+sexuais|direitos\s+reprodutivos|direitos\s+do\s+div[óo]rcio)\b)',
            r'(?=.*\bajuda\s+externa\b)(?=.*\bempoderamento\s+das\s+mulheres\b)',
            r'(?=.*\bmercado\s+global\b)(?=.*\bempoderamento\b)',
            r'(?=.*\bmulher\b)(?=.*\bviol[êe]ncia\b)',
            r'(?=.*\bmenina\w*\b)(?=.*\bviol[êe]ncia\b)',
            r'(?=.*\bacesso\b)(?=.*\bservi[çc]os\s+de\s+planejamento\s+familiar\b)',
            r'(?=.*\bacesso\b)(?=.*\bsa[úu]de\s+reprodutiva\b)'
        ]

    def get_excecoes(self):
        """Define padrões de exclusão."""
        return r''