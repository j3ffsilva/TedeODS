import re

def verifica_expressao(texto):
    texto = texto.lower()  # Normaliza para letras minúsculas
    
    # Define os padrões de busca
    padroes = [
        r'extrema pobreza',
        r'al[íi]vio da pobreza',
        r'erradica[çc][ãa]o da pobreza',
        r'redu[çc][ãa]o da pobreza',
        r'linha internacional de pobreza',
        r'ajuda financeira.*pobreza',
        r'ajuda financeira.*(pobre|pobres)',
        r'ajuda financeira.*divis[ãa]o norte-sul',
        r'desenvolvimento financeiro.*pobreza',
        r'empoderamento financeiro',
        r'efeito[s]? sobre a distribui[çc][ãa]o|efeito[s]? distributivo[s]?',
        r'trabalho infantil',
        r'ajuda ao desenvolvimento',
        r'prote[çc][ãa]o social',
        r'sistema de prote[çc][ãa]o social',
        r'prote[çc][ãa]o social.*acesso',
        r'microfinanc\w*',
        r'resili[êe]ncia dos pobres',
        r'rede de seguran[çc]a.*(pobre[s]?|vulner[áa]vel[eis]*)',
        r'recurso econ[ôo]mico.*acesso',
        r'recursos econ[ôo]micos.*acesso',
        r'banco de alimentos',
        r'bancos de alimentos'
    ]
    
    # Verifica se algum dos padrões aparece no texto e retorna a correspondência
    for p in padroes:
        match = re.search(p, texto)
        if match:
            return True, match.group()
    
    return False, None