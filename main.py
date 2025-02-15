import argparse
import pandas as pd
import importlib
import json
import os
from utils.json_utils import salvar_json


def get_classifier(ods_number):
    """Retorna uma instância do classificador correspondente ao número da ODS."""
    try:
        modulo = importlib.import_module(f"classifiers.ods{str(ods_number).zfill(2)}_classifier")
        class_name = f"ODS{str(ods_number).zfill(2)}Classifier"
        classifier_class = getattr(modulo, class_name)
        return classifier_class()
    except ModuleNotFoundError:
        raise ValueError(f"❌ ODS {ods_number} não implementado. Escolha um número entre 1 e 16.")
    except AttributeError:
        raise ValueError(f"❌ A classe `{class_name}` não foi encontrada no módulo ODS {ods_number}.")


def classify_text(texto):
    """Classifica um texto e retorna o resultado no formato JSON compatível."""
    resultados = {
        "texto": texto,
        "ods": {}
    }
    
    for ods_number in range(1, 17):
        classifier = get_classifier(ods_number)
        resultado, termo_encontrado = classifier.classify(texto)

        if resultado:
            ods_key = f"ods{str(ods_number).zfill(2)}"
            if ods_key not in resultados["ods"]:
                resultados["ods"][ods_key] = []
            resultados["ods"][ods_key].append(termo_encontrado)

    return resultados


def process_text_input(texto, output_file):
    """Processa um texto passado diretamente na linha de comando."""
    resultado_json = classify_text(texto)

    output_path = os.path.join("data", "processed", output_file)  # 🔹 Redireciona para data/processed/
    salvar_json([resultado_json], output_path)


def process_tsv_input(arquivo_tsv, coluna_texto, output_file):
    """Processa um arquivo TSV, classifica os textos e salva o resultado em JSON."""
    if not os.path.exists(arquivo_tsv):
        print(f"❌ Erro: O caminho '{arquivo_tsv}' não é um arquivo válido.")
        return
    
    try:
        df = pd.read_csv(arquivo_tsv, sep="\t")

        if coluna_texto not in df.columns:
            raise KeyError(f"A coluna '{coluna_texto}' não foi encontrada no arquivo TSV.")

        textos = df[coluna_texto].dropna().tolist()
        resultados = [classify_text(texto) for texto in textos]

        output_path = os.path.join("data", "processed", output_file)  # 🔹 Redireciona para data/processed/
        salvar_json(resultados, output_path)

    except Exception as e:
        print(f"⚠️ Erro inesperado ao processar o TSV: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Classifica textos com base nos critérios das ODS.")
    
    # Argumentos de entrada
    parser.add_argument("-i", "--input", type=str, required=True, help="Tipo de entrada: 'texto' ou 'tsv'.")
    parser.add_argument("--texto", type=str, help="Texto a ser classificado (obrigatório se -i texto).")
    parser.add_argument("--tsv", type=str, help="Caminho do arquivo TSV (obrigatório se -i tsv).")
    parser.add_argument("--coluna", type=str, default="Resumo", help="Nome da coluna do TSV que contém o texto.")

    # Argumento de saída
    parser.add_argument("-o", "--output", type=str, required=True, help="Nome do arquivo JSON de saída (será salvo em data/processed/).")

    args = parser.parse_args()

    if args.input == "texto":
        if not args.texto:
            print("❌ Erro: Você deve fornecer um texto com --texto ao usar -i texto.")
        else:
            process_text_input(args.texto, args.output)

    elif args.input == "tsv":
        if not args.tsv:
            print("❌ Erro: Você deve fornecer um arquivo TSV com --tsv ao usar -i tsv.")
        else:
            process_tsv_input(args.tsv, args.coluna, args.output)

    else:
        print("❌ Erro: O parâmetro -i deve ser 'texto' ou 'tsv'.")