import argparse
import pandas as pd
import importlib
import json
import os


def get_classifier(ods_number):
    """Retorna uma instância do classificador correspondente ao número da ODS."""
    try:
        modulo = importlib.import_module(f"classifiers.ods{str(ods_number).zfill(2)}_classifier")
        class_name = f"ODS{str(ods_number).zfill(2)}Classifier"
        classifier_class = getattr(modulo, class_name)
        return classifier_class()
    except ModuleNotFoundError:
        return None
    except AttributeError:
        return None


def classify_text(texto):
    """Classifica um texto e retorna um dicionário com os resultados."""
    resultados = {"ods": {}, "ods_numeros": [], "matches": []}

    for ods_number in range(1, 17):
        classifier = get_classifier(ods_number)
        if classifier:
            resultado, termo_encontrado = classifier.classify(texto)
            if resultado:
                ods_key = f"ods{str(ods_number).zfill(2)}"
                resultados["ods"][ods_key] = termo_encontrado
                resultados["ods_numeros"].append(ods_number)
                resultados["matches"].append(termo_encontrado)

    return resultados


def process_tsv_input(arquivo_tsv, coluna_texto, output_tsv):
    """Processa um arquivo TSV, classifica os textos e salva o resultado em um novo arquivo TSV."""
    if not os.path.exists(arquivo_tsv):
        print(f"❌ Erro: O caminho '{arquivo_tsv}' não é um arquivo válido.")
        return
    
    try:
        df = pd.read_csv(arquivo_tsv, sep="\t")

        if coluna_texto not in df.columns:
            raise KeyError(f"A coluna '{coluna_texto}' não foi encontrada no arquivo TSV.")

        # Criar novas colunas para ODS e Match
        df["ODS"] = ""
        df["Match"] = ""

        for idx, row in df.iterrows():
            resultado = classify_text(row[coluna_texto])
            ods_list = resultado["ods_numeros"]
            matches = resultado["matches"]

            df.at[idx, "ODS"] = f"[{', '.join(map(str, ods_list))}]" if ods_list else "-"
            df.at[idx, "Match"] = "; ".join(matches) if matches else "-"

        # Salvar o arquivo atualizado
        df.to_csv(output_tsv, sep="\t", index=False)
        print(f"✅ Arquivo processado com sucesso: {output_tsv}")

    except Exception as e:
        print(f"⚠️ Erro inesperado ao processar o TSV: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Classifica textos com base nos critérios das ODS e salva o resultado no TSV.")
    
    parser.add_argument("-i", "--tsv", type=str, required=True, help="Caminho do arquivo TSV de entrada.")
    parser.add_argument("--coluna", type=str, default="Resumo", help="Nome da coluna do TSV que contém o texto.")
    parser.add_argument("-o", "--output", type=str, required=True, help="Caminho do arquivo TSV de saída.")

    args = parser.parse_args()

    process_tsv_input(args.tsv, args.coluna, args.output)