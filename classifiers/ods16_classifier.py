from classifiers.base_classifier import BaseODSClassifier

class ODS16Classifier(BaseODSClassifier):
    def __init__(self):
        super().__init__(16)

    def get_padroes(self):
        return [
            # Termos principais
            r'\binoc[êe]ncia\s*presumida\b',
            r'\bfalsa\s*confiss[ãa]o\b',
            r'\bconflito[s]?\s*armado[s]?\b',
            r'\bconflito[s]?\s*civil[íi]s?\b',
            r'\bguerra\b.*\b(conflito|guerra|democracia|Conven[çc][ãa]o\s*de\s*Genebra|tratado|paz)\b',
            r'\bmanuten[çc][ãa]o\s*da\s*paz\b',
            r'\bcorrup[çc][ãa]o\b.*\b(institui[çc][ãa]o|funcion[áa]rio\s*p[úu]blico|governo|suborno|conflito)\b',
            r'\bcrime[s]?\b',
            r'\bcrimin[óo]so[s]?\b',
            r'\bd[éê]ficit\s*democr[áa]tico\b',
            r'\bdemocratiza[çc][ãa]o\b.*\b(institucional|conflito|tomada\s*de\s*decis[ãa]o|sociedade|pol[íi]tica|ajuda\s*financeira)\b',
            r'\bconflito[s]?\s*[ée]tnico[s]?\b',
            r'\bexonera[çc][ãa]o\b',
            r'\bgenoc[íi]dio[s]?\b',
            r'\bhomic[íi]dio[s]?\b',
            r'\bassassinato[s]?\b',
            r'\btr[áa]fico\s*humano\b',
            r'\bsistema\s*de\s*justi[çc]a\s*criminal\b',
            r'\bsistema\s*de\s*justi[çc]a\b',
            r'\bjusti[çc]a\s*arbitr[áa]ria\b',
            r'\brefugiado[s]?\b',
            r'\bterrorista[s]?\b',
            r'\bviol[êe]ncia\b',
            r'\btortura\b',
            r'\bestado\s*de\s*direito\s*efetivo\b',
            r'\bfluxo\s*de\s*armas\b',
            r'\binstitui[çc][ãa]o[s]?\s*transparente[s]?\b',
            r'\bboa\s*governan[çc]a\b',
            r'\bidentidade\s*legal\s*para\s*todos\b',
            r'\bliberdade\s*de\s*informa[çc][ãa]o\b',
            r'\binstitui[çc][ãa]o\s*de\s*direitos\s*humanos\b',
            r'\bativistas\s*de\s*direitos\s*humanos\b',
            r'\bliberdade[s]?\s*fundamental[íi]s?\b',
            r'\bconflito[s]?\s*violentos?\b',
            r'\bsociedade[s]?\s*pac[íi]fica[s]?\b',
            r'\binstitui[çc][ãa]o[s]?\s*efetiva[s]?\b',
            r'\binstitui[çc][ãa]o[s]?\s*respons[áa]vel[eis]?\b',
            r'\binstitui[çc][ãa]o[s]?\s*inclusiva[s]?\b',
            r'\babuso\s*infantil\b',
            r'\bdeten[çc][ãa]o\s*arbitr[áa]ria\b',
            r'\bdeten[çc][ãa]o\s*sem\s*senten[çc]a\b',
            r'\bsistema\s*judicial\b',
            r'\btribunal\s*criminal\b',
            r'\bsociedade[s]?\s*inclusiva[s]?\b',
            r'\brecurso[s]?\s*legal[íi]s?\b',
            r'\bindepend[êe]ncia\s*do\s*judici[áa]rio\b',
            r'\bjudici[áa]rio\s*independente\b',
            r'\bsepara[çc][ãa]o\s*de\s*poderes\b',
            r'\bextremismo\b',
            r'\bcrime\s*de\s*guerra\b',
            r'\bcrime\s*organizado\b',
            r'\btransfer[êe]ncia\s*il[íi]cita\b',
            r'\bdinheiro\s*il[íi]cito\b',
            r'\btr[áa]fico\s*de\s*armas\b',
            r'\bcibercrime|crime[s]?\s*cibern[ée]tico[s]?\b',
            r'\binsurg[êe]ncia\b',
            r'\binstitui[çc][ãa]o\s*democr[áa]tica\b',
            r'\binstabilidade\s*pol[íi]tica\b',
            r'\btomada\s*de\s*decis[ãa]o\s*pol[íi]tica\b.*\b(responsivo|inclusivo|participativo|representativo)\b',
            r'\bConven[çc][ãa]o\s*de\s*Aarhus\b',
            r'\bliberdade\s*de\s*imprensa\b',
            r'\bliberdade\s*de\s*express[ãa]o\b'
        ]

    def get_excecoes(self):
        """Define padrões de exclusão."""
        return r'\b(?:doen[çc]a|gen[ée]tica)\b'