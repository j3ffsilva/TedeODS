import re

def match_terms(text, terms):
    for term in terms:
        if term.startswith('{') and term.endswith('}'):
            term = term[1:-1]  # remove the curly brackets
            if term not in text:
                return False
        elif '*' in term:
            term = term.replace('*', '.*?')  # transform * to its regex equivalent
            if not re.search(term, text):
                return False
        else:
            if term not in text:
                return False
    return True

def evaluate_text(text, expression):
    # Split the expression by the OR operator and then by the AND operator
    or_terms = expression.split(' OU ')
    for or_term in or_terms:
        and_terms = or_term.split(' E ')
        if match_terms(text, and_terms):
            return True
    return False

def match_codes(text, expressions):
    matching_codes = []
    for idx, expression in enumerate(expressions, 1):
        if evaluate_text(text, expression):
            matching_codes.append(f"CÓDIGO {idx}")
    return matching_codes

# List of expressions
expressions = [
    """
     ( ( ( humano E (saúde* OU doença* OU remédio* OU mortalidade ) ) OU {síndrome da criança espancada} OU {doença cardiovascular} OU {doenças cardiovasculares} OU {chagas} OU {abuso infantil } OU {negligência infantil} OU {índice de bem-estar infantil} OU {índice de bem-estar juvenil} OU {doença transmitida pela água} OU {doenças transmitidas pela água} OU {doença tropical} OU {doenças tropicais} OU {doença respiratória crônica} OU {doenças respiratórias crônicas} OU {doença infecciosa} OU {doenças infecciosas} OU {doenças sexualmente transmissíveis} OU {doença sexualmente transmissível} OU {doença transmissível} OU {doenças transmissíveis} OU sida OU aids OU hiv OU {vírus da imunodeficiência humana} OU tuberculose OU malária OU hepatite OU poliomielite* OU vacina* OU câncer* OU diabetes* OU {mortalidade materna} OU {mortalidade infantil} OU {complicações no parto} OU {mortalidade neonatal} OU {mortalidade prematura} OU {mortalidade infantil} OU {ano de vida ajustado pela qualidade} OU {saúde materna} OU {morte evitável} OU {mortes evitáveis} OU {controle do tabaco} OU {abuso de substâncias} OU {abuso de drogas} OU {uso de tabaco} OU {uso de álcool} OU {dependência de substâncias/química} OU {dependência de drogas} OU {tabagismo} OU alcoolismo OU suicídio* OU {depressão pós-parto} OU {zika vírus} OU dengue OU esquistossomose OU {doença do sono} OU ebola OU {saúde mental} OU {transtorno mental} OU { doença mental} OU {doenças mentais} OU {sarampo} OU {doença negligenciada} OU {doenças negligenciadas} OU diarreia OU cólera OU disenteria OU {febre tifoide} OU {acidente de trânsito} OU {acidentes de trânsito} OU {estilo de vida saudável} OU {expectativa de vida} OU {expectativas de vida} OU {política de saúde} OU ( {sistema de saúde} E ( acesso OU acessível ) ) OU {risco de saúde} OU {riscos de saúde} OU {saúde inclusiva} OU obesidade OU {determinantes sociais de saúde} OU {dano psicológico} OU {bem-estar psicológico} OU {bem-estar psicológico} OU {saúde pública} ) )
    """,  # CODE 1
]

text = \
"""
O trabalho a seguir se insere numa proposta geral que visa apresentar aspectos das filosofias de Heráclito e Parmênides através dos cursos ministrados por Bergson na Universidade de Clermont-Ferrand entre 1884 e 1898, período anterior a publicação de sua primeira obra Ensaio sobre os dados imediatos da conesciência. Ressaltaremos a perspectiva de Bergson em relação às doutrinas de Heráclito e Parmênides, de modo a tornar claros os efeitos restauradores de sua interpretação capaz de renovar os conceitos caros a esses filósofos, da mesma forma que torna patente traços de sua filosofia futura. Acreditamos que um estudo aprofundado dos cursos de Bergson contribui tanto para a pesquisa das obras de sua filosofia madura quanto para a pesquisa no campo da filosofia grega
"""

result = match_codes(text, expressions)
print(result)  # ['CÓDIGO 1', 'CÓDIGO 2', ...]
