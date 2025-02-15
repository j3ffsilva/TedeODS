import importlib

def classificar_textos(textos):
    """
    Processa uma lista de textos e classifica-os com base nos ODS.
    Retorna um dicionário estruturado para exportação em JSON.
    """
    resultados = []
    
    # Lista de arquivos que representam os classificadores (ODS 1 a ODS 16)
    ods_scripts = [f'classifiers.ods{str(i).zfill(2)}_classifier' for i in range(1, 17)]
    
    for texto in textos:
        resultado_texto = {
            "texto": texto,
            "classificacoes": []  # Lista de ODS identificadas
        }
        
        for script in ods_scripts:
            try:
                # Importa o módulo dinamicamente
                modulo = importlib.import_module(script)
                
                # Chama a função `verifica_expressao` do módulo
                resultado, expressao = modulo.verifica_expressao(texto)
                
                if resultado:
                    ods_numero = script.split(".")[1].replace("_classifier", "").upper()
                    resultado_texto["classificacoes"].append({
                        "ods": ods_numero,
                        "termos_identificados": expressao
                    })
            except (ModuleNotFoundError, AttributeError) as e:
                print(f"⚠️ Erro ao carregar {script}: {e}")
        
        resultados.append(resultado_texto)
    
    return resultados
