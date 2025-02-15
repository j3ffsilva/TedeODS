import re

def verifica_expressao(texto):
    texto = texto.lower()  # Normaliza para letras minúsculas
    
    # Define os padrões de busca
    padroes = [
        r'igualdade.*(econ[ôo]mica|financeira|socioecon[ôo]mica)',
        r'desigualdade.*(econ[ôo]mica|financeira|socioecon[ôo]mica)',
        r'pol[íi]tica[s]? de reforma econ[ôo]mica',
        r'inclus[ãa]o pol[íi]tica',
        r'pol[íi]tica[s]? de prote[çc][ãa]o social',
        r'imigra[çc][ãa]o(?!.*(qu[íi]mica|doen[çc]a|biodiversidade))',
        r'emigra[çc][ãa]o(?!.*(qu[íi]mica|doen[çc]a|biodiversidade))',
        r'investimento estrangeiro direto',
        r'lacuna[s]? de desenvolvimento',
        r'remessa de migrantes',
        r'migra[çc][ãa]o respons[áa]vel',
        r'pol[íi]tica[s]? de migra[çc][ãa]o|migrat[óo]ria[s]?',
        r'divis[ãa]o norte-sul',
        r'desenvolvimento.*(tarifas?|tarifa zero|acesso isento de impostos)',
        r'exclus[ãa]o social',
        r'marginaliza[çc][ãa]o econ[ôo]mica',
        r'desigualdade de renda',
        r'lei[s]? discriminat[óo]ria[s]?',
        r'pol[íi]tica[s]? discriminat[óo]ria[s]?',
        r'empoderamento econ[ôo]mico',
        r'transforma[çc][ãa]o econ[ôo]mica',
        r'mercado global.*empoderamento'
    ]
    
    # Verifica se algum dos padrões aparece no texto e retorna a correspondência
    for p in padroes:
        match = re.search(p, texto)
        if match:
            return True, match.group()
    
    return False, None