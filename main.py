import argparse
import pandas as pd
import importlib
import os
import json
from tqdm import tqdm


def get_classifier(ods_number):
    """Retorna uma instância do classificador correspondente ao número da ODS."""
    try:
        modulo = importlib.import_module(f"classifiers.ods{str(ods_number).zfill(2)}_classifier")
        class_name = f"ODS{str(ods_number).zfill(2)}Classifier"
        classifier_class = getattr(modulo, class_name)
        return classifier_class()
    except (ModuleNotFoundError, AttributeError):
        return None


def classify_text(texto, ods_number):
    """Classifica um texto para um número específico de ODS e imprime logs para depuração."""
    classifier = get_classifier(ods_number)
    
    if not classifier:
        print(f"⚠️ Classificador ODS{ods_number} não encontrado.")
        return None, None

    print(f"🔍 Rodando classificador {ods_number} para o texto: {texto[:100]}...")

    resultado, termo_encontrado = classifier.classify(texto)

    print(f"✅ Classificador {ods_number} finalizado. Resultado: {resultado}, Termo: {termo_encontrado}")

    if resultado:
        return ods_number, termo_encontrado
    return None, None


def classify_texts(texto):
    """Classifica um texto e retorna um dicionário com os resultados."""
    #resultados = {"ods": {}, "ods_numeros": [], "matches": []}
    resultados = {"ods": []}

    for ods_number in range(1, 17):
        ods, termo = classify_text(texto, ods_number)
        if ods:
            #ods_key = f"ods{str(ods).zfill(2)}"
            #resultados["ods"][ods_key] = ods

            resultados["ods"].append(ods)

    return resultados

def process_tsv_input(arquivo_tsv, coluna_texto, output_json=None, linha_especifica=None, classificador_especifico=None):
    """Processa um arquivo TSV e imprime ou salva os resultados no formato JSON."""
    if not os.path.exists(arquivo_tsv):
        print(f"❌ Erro: O caminho '{arquivo_tsv}' não é um arquivo válido.")
        return
    
    try:
        df = pd.read_csv(arquivo_tsv, sep="\t")

        if coluna_texto not in df.columns:
            raise KeyError(f"A coluna '{coluna_texto}' não foi encontrada no arquivo TSV.")

        if linha_especifica is not None:
            df = df.iloc[[linha_especifica]]  # Filtra apenas a linha desejada

        resultados_finais = []

        for idx, row in tqdm(df.iterrows(), total=len(df), desc="Processando linhas", unit="linha"):
            try:
                texto = row[coluna_texto]
                if not isinstance(texto, str):
                    texto = str(texto)  # Garante que é uma string

                if classificador_especifico is not None:
                    ods, termo = classify_text(texto, classificador_especifico)
                    resultado = {
                        "id": idx,
                        "classificador": classificador_especifico,
                        "ODS": ods if ods else "-",
                        "Match": termo if termo else "-"
                    }
                else:
                    resultado = {
                        "id": idx,
                        **classify_texts(texto)  # Adiciona os resultados completos ao JSON
                    }
                
                resultados_finais.append(resultado)

            except Exception as e:
                print(f"⚠️ Erro ao processar linha {idx}: {e}")

        # Se foi passado um arquivo de saída, salva o JSON nele
        if output_json:
            with open(output_json, "w", encoding="utf-8") as f:
                json.dump(resultados_finais, f, indent=4, ensure_ascii=False)
            print(f"✅ Resultados salvos em '{output_json}'")
        else:
            # Se não foi passado um arquivo de saída, imprime no terminal
            print(json.dumps(resultados_finais, indent=4, ensure_ascii=False))

    except Exception as e:
        print(f"⚠️ Erro inesperado ao processar o TSV: {e}") 


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Classifica textos com base nos critérios das ODS e imprime/salva o resultado no formato JSON.")
    
    parser.add_argument("-i", "--tsv", type=str, required=True, help="Caminho do arquivo TSV de entrada.")
    parser.add_argument("-c", "--coluna", type=str, default="resumo", help="Nome da coluna do TSV que contém o texto.")
    parser.add_argument("-o", "--output", type=str, help="Caminho do arquivo JSON de saída (opcional).")
    parser.add_argument("-l", "--linha", type=int, help="Número da linha específica a processar (começando em 0).")
    parser.add_argument("-k", "--classificador", type=int, help="Número do classificador específico a rodar.")

    args = parser.parse_args()

    process_tsv_input(args.tsv, args.coluna, args.output, args.linha, args.classificador)