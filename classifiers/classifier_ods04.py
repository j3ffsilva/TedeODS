import re

def verifica_expressao(texto):
    texto = texto.lower()  # Normaliza para letras minúsculas
    
    # Grupo principal (deve conter pelo menos um desses termos)
    grupo_principal = [
        r'\bescola\b', r'\beduca[çc][ãa]o\b', r'\beducacional\b'
    ]
    
    # Segundo grupo (deve conter pelo menos um desses termos)
    grupo_secundario = [
        r'\bfrequ[êe]ncia escolar\b',
        r'\bmatr[íi]cula escolar\b',
        r'\beduca[çc][ãa]o inclusiva\b',
        r'\bdesigualdade educacional\b',
        r'\bqualidade educacional\b',
        r'\bmatr[íi]cula educacional\b',
        r'\balfabetiza[çc][ãa]o de adultos\b',
        r'\btaxa de numeramento\b',
        r'\bambiente educacional\b',
        r'\bacesso educacional\b',
        r'\bajuda ao desenvolvimento\b.*\btreinamento de professores\b',
        r'\beduca[çc][ãa]o infantil\b',
        r'\beduca[çc][ãa]o b[áa]sica\b',
        r'\bacess[íi]vel educa[çc][ãa]o\b',
        r'\baux[íi]lio financeiro educacional\b',
        r'\bseguran[çc]a escolar\b',
        r'\bseguran[çc]a na escola\b',
        r'\boportunidades? de aprendizado\b.*\b(disparidades de g[êe]nero|empoderamento)\b',
        r'\bempoderamento da juventude\b',
        r'\bempoderamento das mulheres\b',
        r'\boportunidades iguais\b',
        r'\btrabalho infantil\b',
        r'\bdiscriminat[óo]rio\b',
        r'\blacuna educacional\b',
        r'\barmadilha da pobreza\b.*\bescolaridade\b',
        r'\bnecessidades de educa[çc][ãa]o especial\b',
        r'\bsistema educacional inclusivo\b',
        r'\bescolariza[çc][ãa]o\b.*\b(disparidades de g[êe]nero|disparidades [ée]tnicas|disparidades raciais)\b',
        r'\bexclus[ãa]o educacional\b',
        r'\babandono escolar\b',
        r'\bcidadania global\b',
        r'\beduca[çc][ãa]o para o desenvolvimento sustent[áa]vel\b',
        r'\beduca[çc][ãa]o ambiental\b',
        r'\bpol[ií]tica[s]? educacional[es]?\b',
        r'\beduca[çc][ãa]o internacional\b',
        r'\breforma da educa[çc][ãa]o\b',
        r'\breforma educacional\b.*\bpa[ií]ses em desenvolvimento\b',
        r'\bgovernan[çc]a educacional\b',
        r'\bpa[ií]ses em desenvolvimento\b.*\befeitos escolares\b',
        r'\bdespesas com educa[çc][ãa]o\b',
        r'\bajuda externa\b',
        r'\btreinamento de professores\b.*\bpa[ií]ses em desenvolvimento\b',
        r'\bdesgaste de professores\b'
    ]

    # Exceção (não pode conter)
    excecao = r'\balfabetiza[çc][ãa]o em sa[úu]de\b'
    
    # Se o texto contiver a exceção, retorna False
    if re.search(excecao, texto):
        return False, None
    
    # Verifica se contém pelo menos um termo do grupo principal
    if not any(re.search(p, texto) for p in grupo_principal):
        return False, None

    # Verifica se contém pelo menos um termo do grupo secundário
    for p in grupo_secundario:
        match = re.search(p, texto)
        if match:
            return True, match.group()
    
    return False, None
