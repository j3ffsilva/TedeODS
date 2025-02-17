from classifiers.base_classifier import BaseODSClassifier

class ODS05Classifier(BaseODSClassifier):
    def __init__(self):
        super().__init__(5)

    def get_padroes(self):
        return [
            r'desigualdade de g[êe]nero',
            r'igualdade de g[êe]nero',
            r'igualdade no emprego',
            r'diferen[çc]a salarial entre g[êe]neros',
            r'participa[çc][ãa]o feminina na for[çc]a de trabalho',
            r'participa[çc][ãa]o da[s]? mulher[es]? na for[çc]a de trabalho',
            r'emprego feminino',
            r'desemprego feminino',
            r'acesso.*servi[çc]os de planejamento familiar',
            r'casamento[s]? for[çc]ado[s]?',
            r'casamento[s]? infantil[es]?',
            r'segrega[çc][ãa]o ocupacional',
            r'empoderamento de (mulheres|meninas|feminino)',
            r'mutila[çc][ãa]o genital feminina',
            r'corte genital feminino',
            r'viol[êe]ncia dom[ée]stica',
            r'mulher.*viol[êe]ncia',
            r'menina\w*.*viol[êe]ncia',
            r'viol[êe]ncia sexual',
            r'trabalho (n[ãa]o remunerado|de cuidado n[ãa]o remunerado).*desigualdade de g[êe]nero',
            r'participa[çc][ãa]o pol[íi]tica das mulheres',
            r'participa[çc][ãa]o pol[íi]tica feminina',
            r'gestoras femininas',
            r'mulheres na lideran[çc]a',
            r'lideran[çc]a feminina',
            r'aloca[çc][ãa]o intrafamiliar',
            r'acesso.*sa[úu]de reprodutiva',
            r'assassinato[s]? de honra',
            r'anti-mulheres|antimulheres',
            r'feminismo',
            r'misoginia',
            r'infantic[íi]dio[s]? feminino[s]?',
            r'tr[áa]fico humano',
            r'prostitui[çc][ãa]o for[çc]ada',
            r'igualdade.*(direitos sexuais|direitos reprodutivos|direitos do div[óo]rcio)',
            r'direitos das mulheres',
            r'injusti[çc]a[s]? de g[êe]nero',
            r'discrimina[çc][ãa]o de g[êe]nero',
            r'disparidades de g[êe]nero',
            r'diferen[çc]a de g[êe]nero',
            r'explora[çc][ãa]o feminina',
            r'equidade dom[ée]stica',
            r'sub-representa[çc][ãa]o das mulheres',
            r'empreendedorismo feminino',
            r'propriedade feminina',
            r'desenvolvimento econ[ôo]mico das mulheres',
            r'poder das mulheres',
            r'or[çc]amento sens[íi]vel ao g[êe]nero',
            r'cota de g[êe]nero',
            r'ajuda externa.*empoderamento das mulheres',
            r'segrega[çc][ãa]o de g[êe]nero',
            r'viol[êe]ncia de g[êe]nero',
            r'participa[çc][ãa]o de g[êe]nero',
            r'mulher[es]? na pol[íi]tica',
            r'comportamento contraceptivo',
            r'autonomia das mulheres',
            r'feminismo agr[áa]rio',
            r'microcr[ée]dito',
            r'subsist[êe]ncia das mulheres',
            r'propriedade das mulheres',
            r'pequena propriet[áa]ria',
            r'transversaliza[çc][ãa]o de g[êe]nero'
        ]
    
    def get_excecoes(self):
        """Define padrões de exclusão."""
        return r''