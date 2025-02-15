import os
import importlib
import json
import pandas as pd

def verifica_texto_ods(textos):
    resultados = []
    
    # Lista de arquivos que representam as ODS (ODS 1 a ODS 16)
    ods_scripts = [f'parser_ods{str(i).zfill(2)}' for i in range(1, 17)]
    
    for texto in textos:
        resultado_texto = {"texto": texto, "ods": {}}
        
        for script in ods_scripts:
            try:
                # Importa o módulo dinamicamente
                modulo = importlib.import_module(script)
                
                # Chama a função verifica_expressao do módulo
                resultado, expressao = modulo.verifica_expressao(texto)
                
                if resultado:
                    ods_key = script.replace("parser_", "").lower()
                    if ods_key not in resultado_texto["ods"]:
                        resultado_texto["ods"][ods_key] = []
                    resultado_texto["ods"][ods_key].append(expressao)
            except (ModuleNotFoundError, AttributeError) as e:
                print(f"Erro ao carregar {script}: {e}")
        
        resultados.append(resultado_texto)
    
    return json.dumps(resultados, indent=4, ensure_ascii=False)

# Carregar o arquivo pipeq.tsv e processar os textos
arquivo_tsv = "parser/pipeq.tsv"
df = pd.read_csv(arquivo_tsv, sep="\t")

# Verificar se a coluna 'Resumo' existe
if "Resumo" in df.columns:
    textos = df["Resumo"].dropna().tolist()
    resultado_ods = verifica_texto_ods(textos)
    
    # Salvar resultado em JSON
    with open("resultado_ods.json", "w", encoding="utf-8") as f:
        f.write(resultado_ods)
    
    print("Arquivo 'resultado_ods.json' gerado com sucesso!")
else:
    print("Erro: A coluna 'Resumo' não foi encontrada no arquivo TSV.")