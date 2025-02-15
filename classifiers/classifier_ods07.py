import re

def verifica_expressao(texto):
    texto = texto.lower()  # Normaliza para letras minúsculas
    
    # Define os padrões de busca
    padroes = [
        r'efici[êe]ncia energ[ée]tica',
        r'consumo de energia',
        r'transi[çc][ãa]o energ[ée]tica',
        r'tecnologia de energia limpa',
        r'equidade energ[ée]tica',
        r'justi[çc]a energ[ée]tica',
        r'pobreza energ[ée]tica',
        r'pol[íi]tica energ[ée]tica',
        r'renov[áa]vel\w*',
        r'sociedade de 2000 watts',
        r'micro-rede inteligente',
        r'rede inteligente',
        r'microrrede inteligente',
        r'micro-redes inteligentes',
        r'redes inteligentes',
        r'microrredes inteligentes',
        r'medidor inteligente',
        r'medidores inteligentes',
        r'eletricidade acess[íi]vel',
        r'consumo de eletricidade',
        r'eletricidade confi[áa]vel',
        r'combust[íi]vel limpo',
        r'combust[íi]vel limpo para cozinhar',
        r'pobreza de combust[íi]vel',
        r'energiewende',
        r'avalia[çc][ãa]o do ciclo de vida',
        r'avalia[çc][õo]es do ciclo de vida',
        r'fotoqu[íi]mica.*energia renov[áa]vel',
        r'fotovoltaica',
        r'divis[ãa]o fotocatal[íi]tica da [áa]gua',
        r'produ[çc][ãa]o de hidrog[êe]nio',
        r'divis[ãa]o da [áa]gua',
        r'bateria[s]? de [íi]on-l[íi]tio',
        r'rede de calor',
        r'calor distrital',
        r'aquecimento distrital',
        r'consumo de energia (residencial|dom[ée]stica)',
        r'seguran[çc]a energ[ée]tica',
        r'eletrifica[çc][ãa]o rural',
        r'escada de energia',
        r'acesso [àa] energia',
        r'conserva[çc][ãa]o de energia',
        r'sociedade de baixo carbono',
        r'sistema[s]? h[íi]brido[s]? de energia renov[áa]vel',
        r'troca de combust[íi]vel',
        r'ajuda externa (ao|para o) desenvolvimento.*energia renov[áa]vel',
        r'governan[çc]a energ[ée]tica',
        r'assist[êe]ncia oficial ao desenvolvimento.*eletricidade',
        r'desenvolvimento energ[ée]tico.*pa[ií]ses em desenvolvimento'
    ]
    
    # Exceções (não pode conter "rede de sensores sem fio")
    if re.search(r'rede[s]? de sensores sem fio', texto):
        return False, None
    
    # Verifica se algum dos padrões aparece no texto e retorna a correspondência
    for p in padroes:
        match = re.search(p, texto)
        if match:
            return True, match.group()
    
    return False, None