import re

def verifica_expressao(texto):
    texto = texto.lower()  # Normaliza para letras minúsculas
    
    # Define os padrões de busca
    padroes = [
        r'direitos de posse da terra',
        r'pequeno produtor.*(fazenda|silvicultura|pastoril|agricultura|pesca|produtor de alimentos|produtores de alimentos)',
        r'desnutri[çc][ãa]o',
        r'desnutrid[o|a]',
        r'subnutri[çc][ãa]o',
        r'subnutrid[o|a]',
        r'produ[çc][ãa]o agr[íi]cola',
        r'produtividade agr[íi]cola',
        r'pr[áa]ticas agr[íi]colas',
        r'manejo|gest[ãa]o agr[íi]cola',
        r'produ[çc][ãa]o alimentar|de alimentos',
        r'produtividade alimentar|de alimentos',
        r'seguran[çc]a alimentar',
        r'inseguran[çc]a alimentar',
        r'direito[s]? [àa] terra',
        r'reforma agr[áa]ria',
        r'reformas agr[áa]rias',
        r'pr[áa]ticas agr[íi]colas resilientes',
        r'agricultura.*pot[áa]ssio',
        r'fertilizante',
        r'melhoria da nutri[çc][ãa]o alimentar',
        r'fome oculta',
        r'alimentos geneticamente modificados',
        r'transg[êe]nicos.*alimentos',
        r'pr[áa]ticas agroflorestais',
        r'manejo|gest[ãa]o agroflorestal',
        r'inova[çc][ãa]o agr[íi]cola',
        r'seguran[çc]a alimentar.*diversidade gen[ée]tica',
        r'mercado de alimentos.*(restri[çc][ãa]o|tarifa|acesso|divis[ãa]o norte-sul|governan[çc]a do desenvolvimento)',
        r'governan[çc]a alimentar',
        r'cadeia de abastecimento alimentar',
        r'cadeia de valor alimentar',
        r'mercado de commodities alimentares'
    ]
    
    # Exceções (não pode conter "doença")
    if re.search(r'doen[çc]a', texto):
        return False, None
    
    # Verifica se algum dos padrões aparece no texto e retorna a correspondência
    for p in padroes:
        match = re.search(p, texto)
        if match:
            return True, match.group()
    
    return False, None