import csv
import json

def csv_para_json(csv_file, json_file):
    dados = []

    with open(csv_file, mode='r', encoding='utf-8') as f:
        leitor_csv = csv.DictReader(f, delimiter='\t')
        
        # Itera sobre cada linha do CSV e transforma em um dicionário
        for linha in leitor_csv:
            # Converte a coluna ODS para uma lista de inteiros
            ods_list = [
                int(x.strip()) for x in linha["ODS"].split(",") if x.strip().isdigit()
            ]

            # Converte as palavras-chave para listas (verifica se não estão vazias)
            palavras_chave = [
                p.strip() for p in linha["palavras_chave"].split("|") if p.strip()
            ]
            keywords = [
                k.strip() for k in linha["keywords"].split("|") if k.strip()
            ]

            # Monta o dicionário final para cada registro
            dados.append({
                "data": linha["data"],
                "titulo": linha["titulo"],
                "resumo": linha["resumo"],
                "abstract": linha["abstract"],
                "palavras_chave": palavras_chave,
                "keywords": keywords,
                "ODS": ods_list
            })

    # Escreve os dados em formato JSON
    with open(json_file, mode='w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

# Executa a conversão
csv_para_json(
    r'.\data\teses-e-dissertações-ods.tsv',
    r'.\data\teses-e-dissertações-ods.json'
)