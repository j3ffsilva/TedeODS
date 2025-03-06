import re

class BaseODSClassifier:
    def __init__(self, ods_number):
        self.ods_number = ods_number
        self.name = f"ODS {ods_number}"
        self.padroes = self.get_padroes()
        self.excecao = self.get_excecoes()

    def get_padroes(self):
        """Cada subclassificador deve definir seus próprios padrões de busca."""
        raise NotImplementedError("Cada subclassificador deve definir `get_padroes`")

    def get_excecoes(self):
        """Define padrões de exclusão (se aplicável)."""
        raise NotImplementedError("Cada subclassificador deve definir `get_exceções`")

    def classify(self, texto):
        """Verifica se o texto contém os padrões esperados, respeitando exceções e capturando a substring detectada."""
        texto = texto.lower().strip()

        # Se o texto contiver a exceção, retorna False
        if self.excecao and re.search(self.excecao, texto, re.IGNORECASE):
            return False, None

        # Verifica cada padrão
        for p in self.padroes:
            # Lookahead para validar a presença do padrão
            if re.search(p, texto, re.IGNORECASE | re.MULTILINE):
                # Captura do contexto completo com até 3 palavras antes e depois do padrão
                captura = re.search(r'((?:\w+\s*){0,1}' + p + r'(?:\s*\w+){0,1})', texto, re.IGNORECASE)
                
                if captura:
                    return True, captura.group(1)  # Retorna o contexto capturado

        return False, None