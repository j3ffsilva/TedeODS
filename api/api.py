from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

# Carrega o dataset JSON ao iniciar a API
with open(r'./data/dataset-ods.json', "r", encoding="utf-8") as f:
    data = json.load(f)

# Função para filtrar dados por critério
def filtrar_dados(query_params):
    resultados = data
    for chave, valor in query_params.items():
        if chave == "data":
            try:
                # Converte a data fornecida na query e no dataset para objetos datetime
                data_query = datetime.strptime(valor, "%Y-%m-%d")
                resultados = [
                    item for item in resultados 
                    if datetime.strptime(item["data"], "%m/%d/%Y") == data_query
                ]
            except ValueError:
                return []  # Retorna lista vazia se a data não puder ser convertida
        elif chave == "palavra_resumo":
            resultados = [item for item in resultados if valor.lower() in item["resumo"].lower()]
        elif chave == "ods":
            try:
                valor_int = int(valor)
                resultados = [item for item in resultados if valor_int in item["ODS"]]
            except ValueError:
                return []
        elif chave == "palavra_chave":
            resultados = [
                item for item in resultados
                if any(valor.lower() in p.lower() for p in item["palavras_chave"])
            ]
    return resultados

# Rota para buscar informações por filtros
@app.route("/buscar", methods=["GET"])
def buscar():
    query_params = request.args
    resultados = filtrar_dados(query_params)
    return jsonify(resultados), 200

# Inicia o servidor
if __name__ == "__main__":
    app.run(debug=False)