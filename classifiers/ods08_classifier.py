from classifiers.base_classifier import BaseODSClassifier

class ODS08Classifier(BaseODSClassifier):
    def __init__(self):
        super().__init__(8)

    def get_padroes(self):
        return [
            r'crescimento econ[ôo]mico',
            r'pol[íi]tica de desenvolvimento econ[ôo]mico',
            r'pol[íi]tica de emprego',
            r'crescimento econ[ôo]mico inclusivo',
            r'crescimento sustent[áa]vel',
            r'desenvolvimento econ[ôo]mico',
            r'globaliza[çc][ãa]o econ[ôo]mica',
            r'produtividade econ[ôo]mica',
            r'economia de baixo carbono',
            r'crescimento inclusivo',
            r'microcr[ée]dito\w*',
            r'renda igual',
            r'sal[áa]rios iguais',
            r'emprego[s]? decente[s]?',
            r'emprego[s]? de qualidade',
            r'cria[çc][ãa]o de emprego',
            r'pleno emprego',
            r'prote[çc][ãa]o do emprego',
            r'emprego[s]? informal[es]?',
            r'emprego[s]? prec[áa]rio[s]?',
            r'desemprego',
            r'trabalho[s]? prec[áa]rio[s]?',
            r'microempresa\w*',
            r'pequena empresa',
            r'm[ée]dia empresa',
            r'pequenas empresas',
            r'm[ée]dias empresas',
            r'pequeno[s]? empres[áa]rio[s]?',
            r'empres[áa]rio[s]? iniciante[s]?',
            r'm[ée]dio[s]? empres[áa]rio[s]?',
            r'pequeno[s]? empreendedor[es]?',
            r'm[ée]dio[s]? empreendedor[es]?',
            r'empreendedor[es]? iniciante[s]?',
            r'empreendedorismo social',
            r'ambiente de trabalho seguro',
            r'institui[çc][ãa]o do mercado de trabalho',
            r'institui[çc][õo]es do mercado de trabalho',
            r'trabalho for[çc]ado',
            r'trabalho infantil',
            r'direito[s]? trabalhista[s]?',
            r'escravid[ãa]o moderna',
            r'tr[áa]fico de pessoas',
            r'crianc[aã]-soldado',
            r'crian[çc]as-soldado',
            r'emprego[s]? global[es]?',
            r'sal[áa]rio m[íi]nimo',
            r'economia circular',
            r'economia inclusiva',
            r'economia rural',
            r'investimento de desenvolvimento estrangeiro',
            r'ajuda ao com[ée]rcio',
            r'sindicatos?',
            r'trabalhadores pobres',
            r'n[ãa]o est[áa] em educa[çc][ãa]o, emprego ou treinamento',
            r'compensa[çc][ãa]o de carbono',
            r'projeto[s]? de compensa[çc][ãa]o',
            r'diversifica[çc][ãa]o econ[ôo]mica',
            r'pegada material',
            r'efici[êe]ncia de recursos',
            r'ber[çc]o ao ber[çc]o.*economia',
            r'dissocia[çc][ãa]o econ[ôo]mica',
            r'disparidades do mercado de trabalho',
            r'turismo sustent[áa]vel',
            r'ecoturismo',
            r'turismo baseado na comunidade',
            r'emprego no turismo',
            r'pol[íi]tica de turismo sustent[áa]vel',
            r'acesso financeiro',
            r'inclus[ãa]o financeira',
            r'acesso a servi[çc]os banc[áa]rios'
        ]
    
    def get_excecoes(self):
        """Define padrões de exclusão."""
        return r''