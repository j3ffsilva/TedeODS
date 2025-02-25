from classifiers.base_classifier import BaseODSClassifier

class ODS07Classifier(BaseODSClassifier):
    def __init__(self):
        super().__init__(7)

    def get_padroes(self):
        return [
            r'efici[êe]ncia\s*energ[ée]tica',
            r'consumo\s*de\s*energia',
            r'transi[çc][ãa]o\s*energ[ée]tica',
            r'tecnologia\s*de\s*energia\s*limpa',
            r'equidade\s*energ[ée]tica',
            r'justi[çc]a\s*energ[ée]tica',
            r'pobreza\s*energ[ée]tica',
            r'pol[íi]tica\s*energ[ée]tica',
            r'renov[áa]vel\w*',
            r'sociedade\s*de\s*2000\s*watts',
            r'micro-rede\s*inteligente',
            r'rede\s*inteligente',
            r'microrrede\s*inteligente',
            r'micro-redes\s*inteligentes',
            r'redes\s*inteligentes',
            r'microrredes\s*inteligentes',
            r'medidor\s*inteligente',
            r'medidores\s*inteligentes',
            r'eletricidade\s*acess[íi]vel',
            r'consumo\s*de\s*eletricidade',
            r'eletricidade\s*confi[áa]vel',
            r'combust[íi]vel\s*limpo',
            r'combust[íi]vel\s*limpo\s*para\s*cozinhar',
            r'pobreza\s*de\s*combust[íi]vel',
            r'energiewende',
            r'avalia[çc][ãa]o\s*do\s*ciclo\s*de\s*vida',
            r'avalia[çc][õo]es\s*do\s*ciclo\s*de\s*vida',
            r'fotoqu[íi]mica.*energia\s*renov[áa]vel',
            r'fotovoltaica',
            r'divis[ãa]o\s*fotocatal[íi]tica\s*da\s*[áa]gua',
            r'produ[çc][ãa]o\s*de\s*hidrog[êe]nio',
            r'divis[ãa]o\s*da\s*[áa]gua',
            r'bateria[s]?\s*de\s*[íi]on-l[íi]tio',
            r'rede\s*de\s*calor',
            r'calor\s*distrital',
            r'aquecimento\s*distrital',
            r'consumo\s*de\s*energia\s*(residencial|dom[ée]stica)',
            r'seguran[çc]a\s*energ[ée]tica',
            r'eletrifica[çc][ãa]o\s*rural',
            r'escada\s*de\s*energia',
            r'acesso\s*[àa]\s*energia',
            r'conserva[çc][ãa]o\s*de\s*energia',
            r'sociedade\s*de\s*baixo\s*carbono',
            r'sistema[s]\s* h[íi]brido[s]?\s*de\s*energia\s*renov[áa]vel',
            r'troca\s*de\s*combust[íi]vel',
            r'ajuda externa\s*(ao|para\s*o)\s*desenvolvimento.*energia\s*renov[áa]vel',
            r'governan[çc]a\s*energ[ée]tica',
            r'assist[êe]ncia\s*oficial\s*ao\s*desenvolvimento.*eletricidade',
            r'desenvolvimento\s*energ[ée]tico.*pa[ií]ses\s*em\s*desenvolvimento'
        ]
    
    def get_excecoes(self):
        """Define padrões de exclusão."""
        return r''