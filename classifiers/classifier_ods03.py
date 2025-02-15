import re

def verifica_expressao(texto):
    texto = texto.lower()  # Normaliza para letras minúsculas
    
    # Define os padrões de busca
    padroes = [
        r'humano.*(sa[úu]de\w*|doen[çc]a\w*|rem[ée]dio\w*|mortalidade)',
        r's[íi]ndrome da crian[çc]a espancada',
        r'doen[çc]a[s]? cardiovascular[es]?',
        r'chagas',
        r'abuso infantil',
        r'neglig[êe]ncia infantil',
        r'[íi]ndice de bem-estar (infantil|juvenil)',
        r'doen[çc]a[s]? transmitida[s]? pela [áa]gua',
        r'doen[çc]a[s]? tropical[es]?',
        r'doen[çc]a[s]? respirat[óo]ria[s]? cr[ôo]nica[s]?',
        r'doen[çc]a[s]? infecciosa[s]?',
        r'doen[çc]a[s]? sexualmente transmiss[ií]vel[eis]?',
        r'doen[çc]a[s]? transmiss[ií]vel[eis]?',
        r'sida|aids|hiv|v[ií]rus da imunodefici[êe]ncia humana',
        r'tuberculose',
        r'mal[áa]ria',
        r'hepatite',
        r'poliomielite\w*',
        r'vacina\w*',
        r'c[âa]ncer\w*',
        r'diabetes\w*',
        r'mortalidade (materna|infantil|neonatal|prematura)',
        r'complica[çc][õo]es no parto',
        r'ano de vida ajustado pela qualidade',
        r'sa[úu]de materna',
        r'morte[s]? evit[áa]vel[eis]?',
        r'controle do tabaco',
        r'abuso de (subst[âa]ncias|drogas)',
        r'uso de (tabaco|[áa]lcool)',
        r'depend[êe]ncia de (subst[âa]ncias|qu[ií]mica|drogas)',
        r'tabagismo|alcoolismo',
        r'suic[ií]dio\w*',
        r'depress[ãa]o p[óo]s-parto',
        r'(zika v[ií]rus|dengue|esquistossomose|doen[çc]a do sono|ebola)',
        r'sa[úu]de mental',
        r'transtorno[s]? mental[es]?',
        r'doen[çc]a[s]? mental[es]?',
        r'sarampo',
        r'doen[çc]a[s]? negligenciada[s]?',
        r'diarreia|c[óo]lera|disenteria|febre tifoide',
        r'acidente[s]? de tr[âa]nsito',
        r'estilo de vida saud[áa]vel',
        r'expectativa[s]? de vida',
        r'pol[íi]tica de sa[úu]de',
        r'sistema de sa[úu]de.*(acesso|acess[ií]vel)',
        r'risco[s]? de sa[úu]de',
        r'sa[úu]de inclusiva',
        r'obesidade',
        r'determinantes sociais de sa[úu]de',
        r'dano psicol[óo]gico',
        r'bem-estar psicol[óo]gico',
        r'sa[úu]de p[úu]blica'
    ]
    
    # Verifica se algum dos padrões aparece no texto e retorna a correspondência
    for p in padroes:
        match = re.search(p, texto)
        if match:
            return True, match.group()
    
    return False, None