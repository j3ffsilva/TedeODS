import json
import os

def salvar_json(dados, caminho_arquivo):
    """Salva os dados em um arquivo JSON de forma organizada, criando diretórios se necessário."""
    try:
        # Criar diretório se não existir
        diretorio = os.path.dirname(caminho_arquivo)
        if diretorio and not os.path.exists(diretorio):
            os.makedirs(diretorio)

        # Salvar JSON
        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
        
        print(f"✅ Arquivo JSON salvo com sucesso: {caminho_arquivo}")
    
    except Exception as e:
        print(f"❌ Erro ao salvar JSON: {e}")
