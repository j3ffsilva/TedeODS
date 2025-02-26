from classifiers.base_classifier import BaseODSClassifier

class ODS16Classifier(BaseODSClassifier):
    def __init__(self):
        super().__init__(16)

    def get_padroes(self):
        return [
            # Expressões ajustadas para ordem flexível usando lookaheads
            r'(?=.*\b(?:inoc[êe]ncia|presumida)\b)(?=.*\b(?:inoc[êe]ncia|presumida)\b)',
            r'(?=.*\b(?:falsa|confiss[ãa]o)\b)(?=.*\b(?:falsa|confiss[ãa]o)\b)',
            r'(?=.*\b(?:conflito[s]?|armado[s]?)\b)(?=.*\b(?:conflito[s]?|armado[s]?)\b)',
            r'(?=.*\b(?:conflito[s]?|civil[íi]s?)\b)(?=.*\b(?:conflito[s]?|civil[íi]s?)\b)',
            r'(?=.*\b(?:guerra|conflito|democracia|Conven[çc][ãa]o.*?Genebra|tratado|paz)\b)(?=.*\bguerra\b)',
            r'(?=.*\b(?:manuten[çc][ãa]o|paz)\b)(?=.*\b(?:manuten[çc][ãa]o|paz)\b)',
            r'(?=.*\b(?:corrup[çc][ãa]o|institui[çc][ãa]o|funcion[áa]rio.*?p[úu]blico|governo|suborno|conflito)\b)(?=.*\bcorrup[çc][ãa]o\b)',
            r'\bcrime[s]?\b',
            r'\bcrimin[óo]so[s]?\b',
            r'(?=.*\b(?:d[éê]ficit|democr[áa]tico)\b)(?=.*\b(?:d[éê]ficit|democr[áa]tico)\b)',
            r'(?=.*\b(?:democratiza[çc][ãa]o|institucional|conflito|tomada.*?decis[ãa]o|sociedade|pol[íi]tica|ajuda.*?financeira)\b)(?=.*\bdemocratiza[çc][ãa]o\b)',
            r'(?=.*\b(?:conflito[s]?|[ée]tnico[s]?)\b)(?=.*\b(?:conflito[s]?|[ée]tnico[s]?)\b)',
            r'\bexonera[çc][ãa]o\b',
            r'\bgenoc[íi]dio[s]?\b',
            r'\bhomic[íi]dio[s]?\b',
            r'\bassassinato[s]?\b',
            r'(?=.*\b(?:tr[áa]fico|humano)\b)(?=.*\b(?:tr[áa]fico|humano)\b)',
            r'(?=.*\b(?:sistema|justi[çc]a|criminal)\b)(?=.*\b(?:sistema|justi[çc]a|criminal)\b)',
            r'(?=.*\b(?:justi[çc]a|arbitr[áa]ria)\b)(?=.*\b(?:justi[çc]a|arbitr[áa]ria)\b)',
            r'\brefugiado[s]?\b',
            r'\bterrorista[s]?\b',
            r'\bviol[êe]ncia\b',
            r'\btortura\b',
            r'(?=.*\b(?:estado|direito|efetivo)\b)(?=.*\b(?:estado|direito|efetivo)\b)',
            r'(?=.*\b(?:fluxo|armas)\b)(?=.*\b(?:fluxo|armas)\b)',
            r'(?=.*\b(?:institui[çc][ãa]o[s]?|transparente[s]?)\b)(?=.*\b(?:institui[çc][ãa]o[s]?|transparente[s]?)\b)',
            r'(?=.*\b(?:boa|governan[çc]a)\b)(?=.*\b(?:boa|governan[çc]a)\b)',
            r'(?=.*\b(?:identidade|legal|todos)\b)(?=.*\b(?:identidade|legal|todos)\b)',
            r'(?=.*\b(?:liberdade|informa[çc][ãa]o)\b)(?=.*\b(?:liberdade|informa[çc][ãa]o)\b)',
            r'(?=.*\b(?:institui[çc][ãa]o|direitos|humanos)\b)(?=.*\b(?:institui[çc][ãa]o|direitos|humanos)\b)',
            r'(?=.*\b(?:ativistas|direitos|humanos)\b)(?=.*\b(?:ativistas|direitos|humanos)\b)',
            r'(?=.*\b(?:liberdade[s]?|fundamental[íi]s?)\b)(?=.*\b(?:liberdade[s]?|fundamental[íi]s?)\b)',
            r'(?=.*\b(?:conflito[s]?|violento[s]?)\b)(?=.*\b(?:conflito[s]?|violento[s]?)\b)',
            r'(?=.*\b(?:sociedade[s]?|pac[íi]fica[s]?)\b)(?=.*\b(?:sociedade[s]?|pac[íi]fica[s]?)\b)',
            r'(?=.*\b(?:institui[çc][ãa]o[s]?|efetiva[s]?)\b)(?=.*\b(?:institui[çc][ãa]o[s]?|efetiva[s]?)\b)',
            r'(?=.*\b(?:institui[çc][ãa]o[s]?|respons[áa]vel[eis]?)\b)(?=.*\b(?:institui[çc][ãa]o[s]?|respons[áa]vel[eis]?)\b)',
            r'(?=.*\b(?:institui[çc][ãa]o[s]?|inclusiva[s]?)\b)(?=.*\b(?:institui[çc][ãa]o[s]?|inclusiva[s]?)\b)',
            r'\babuso\s*infantil\b',
            r'(?=.*\b(?:deten[çc][ãa]o|arbitr[áa]ria)\b)(?=.*\b(?:deten[çc][ãa]o|arbitr[áa]ria)\b)',
            r'(?=.*\b(?:deten[çc][ãa]o|sem|senten[çc]a)\b)(?=.*\b(?:deten[çc][ãa]o|sem|senten[çc]a)\b)',
            r'\bsistema\s*judicial\b',
            r'\btribunal\s*criminal\b',
            r'(?=.*\b(?:sociedade[s]?|inclusiva[s]?)\b)(?=.*\b(?:sociedade[s]?|inclusiva[s]?)\b)',
            r'(?=.*\b(?:recurso[s]?|legal[íi]s?)\b)(?=.*\b(?:recurso[s]?|legal[íi]s?)\b)',
            r'(?=.*\b(?:independ[êe]ncia|judici[áa]rio)\b)(?=.*\b(?:independ[êe]ncia|judici[áa]rio)\b)',
            r'(?=.*\b(?:separa[çc][ãa]o|poderes)\b)(?=.*\b(?:separa[çc][ãa]o|poderes)\b)',
            r'\bextremismo\b',
            r'(?=.*\b(?:crime|guerra)\b)(?=.*\b(?:crime|guerra)\b)',
            r'(?=.*\b(?:crime|organizado)\b)(?=.*\b(?:crime|organizado)\b)',
            r'(?=.*\b(?:transfer[êe]ncia|il[íi]cita)\b)(?=.*\b(?:transfer[êe]ncia|il[íi]cita)\b)',
            r'(?=.*\b(?:dinheiro|il[íi]cito)\b)(?=.*\b(?:dinheiro|il[íi]cito)\b)',
            r'(?=.*\b(?:tr[áa]fico|armas)\b)(?=.*\b(?:tr[áa]fico|armas)\b)',
            r'\b(?:cibercrime|crime[s]?.*?cibern[ée]tico[s]?)\b',
            r'\binsurg[êe]ncia\b',
            r'(?=.*\b(?:institui[çc][ãa]o|democr[áa]tica)\b)(?=.*\b(?:institui[çc][ãa]o|democr[áa]tica)\b)',
            r'(?=.*\b(?:instabilidade|pol[íi]tica)\b)(?=.*\b(?:instabilidade|pol[íi]tica)\b)',
            r'(?=.*\b(?:tomada|decis[ãa]o|pol[íi]tica)\b)(?=.*\b(?:responsivo|inclusivo|participativo|representativo)\b)',
            r'(?=.*\b(?:Conven[çc][ãa]o|Aarhus)\b)(?=.*\b(?:Conven[çc][ãa]o|Aarhus)\b)',
            r'(?=.*\b(?:liberdade|imprensa)\b)(?=.*\b(?:liberdade|imprensa)\b)',
            r'(?=.*\b(?:liberdade|express[ãa]o)\b)(?=.*\b(?:liberdade|express[ãa]o)\b)'
        ]

    def get_excecoes(self):
        """Define padrões de exclusão."""
        return r'\b(?:doen[çc]a|gen[ée]tica)\b'