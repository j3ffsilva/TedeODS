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
        texto = texto.lower().strip()  # Normaliza para letras minúsculas e remove espaços extras

        # Se o texto contiver a exceção, retorna False
        if self.excecao and re.search(self.excecao, texto, re.IGNORECASE):
            return False, None

        # Verifica cada padrão
        for p in self.padroes:
            match = re.search(p, texto, re.IGNORECASE | re.MULTILINE)
            if match:
                return True, match.group(0)  # Captura a correspondência completa
        
        return False, None