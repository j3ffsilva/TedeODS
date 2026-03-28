from classifiers.base_classifier import BaseODSClassifier

class ODS17Classifier(BaseODSClassifier):
    def __init__(self):
        super().__init__(17)

    def get_padroes(self):
        return [
            # Cooperação internacional
            r'\bcoopera[cç][aã]o\s+internacional\b',
            r'\bcoopera[cç][aã]o\s+para\s+o\s+desenvolvimento\b',
            r'\bcoopera[cç][aã]o\s+norte[\s\-]sul\b',
            r'\bcoopera[cç][aã]o\s+sul[\s\-]sul\b',
            r'\bcoopera[cç][aã]o\s+triangular\b',

            # Ajuda ao desenvolvimento
            r'\bajuda\s+ao\s+desenvolvimento\b',
            r'\bajuda\s+externa\b',
            r'\bajuda\s+oficial\s+ao\s+desenvolvimento\b',
            r'\bassist[eê]ncia\s+oficial\s+ao\s+desenvolvimento\b',

            # Financiamento
            r'\bfinanciamento\s+do\s+desenvolvimento\b',
            r'\bfluxos\s+financeiros\s+internacionais\b',
            r'\bsistema\s+financeiro\s+internacional\b',
            r'\binvestimento\s+estrangeiro\s+direto\b',

            # Dívida
            r'\bd[ií]vida\s+externa\b',
            r'\bal[ií]vio\s+da\s+d[ií]vida\b',
            r'\breestrutura[cç][aã]o\s+da\s+d[ií]vida\b',

            # Transferência de tecnologia
            r'\btransfer[eê]ncia\s+de\s+tecnologia\b',
            r'\btransfer[eê]ncia\s+tecnol[oó]gica\b',

            # Parcerias para o desenvolvimento
            r'\bparcerias?\s+para\s+o\s+desenvolvimento\b',

            # Governança e multilateralismo
            r'\bgovern[aâ]n[cç]a\s+global\b',
            r'\bmultilateralismo\b',
            r'\bacordos?\s+multilaterais?\b',
            r'\bsistema\s+multilateral\s+de\s+com[eé]rcio\b',

            # Comércio internacional
            r'\bcom[eé]rcio\s+internacional\b',
            r'\bfacilita[cç][aã]o\s+do\s+com[eé]rcio\b',

            # Agenda 2030 e ODS
            r'\bagenda\s+2030\b',
            r'\bimplementa[cç][aã]o\s+dos\s+ods\b',
            r'\bmeios\s+de\s+implementa[cç][aã]o\b',
            r'\bcoer[eê]ncia\s+de\s+pol[ií]ticas\b',
            r'\bmonitoramento\s+dos\s+ods\b',
            r'\bindicadores\s+dos\s+ods\b',

            # Organizações financeiras internacionais
            r'\bfundo\s+monet[aá]rio\s+internacional\b',
            r'\borgani[sz]a[cç][aã]o\s+mundial\s+do\s+com[eé]rcio\b',

            # Revisões voluntárias
            r'\brevis[aã]o\s+volunt[aá]ria\s+nacional\b',
            r'\brevis[aã]o\s+local\s+volunt[aá]ria\b',

            # Expressões com E (qualquer ordem)
            r'(?=.*\bcoopera[cç][aã]o\b)(?=.*\bdesenvolvimento\s+sustent[aá]vel\b)',
            r'(?=.*\bfinanciamento\b)(?=.*\bobjetivos\s+de\s+desenvolvimento\s+sustent[aá]vel\b)',
            r'(?=.*\bparceria\b)(?=.*\bobjetivos\s+de\s+desenvolvimento\s+sustent[aá]vel\b)',
            r'(?=.*\bcom[eé]rcio\b)(?=.*\bpa[íi]ses\s+em\s+desenvolvimento\b)',
            r'(?=.*\btransfer[eê]ncia\b)(?=.*\btecnologia\b)(?=.*\bpa[íi]ses\s+em\s+desenvolvimento\b)',
        ]

    def get_excecoes(self):
        return r''