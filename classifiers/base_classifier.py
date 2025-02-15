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
        return r'\balfabetiza[çc][ãa]o em sa[úu]de\b'

    def classify(self, texto):
        """Verifica se o texto contém os padrões esperados, respeitando exceções."""
        texto = texto.lower()  # Normaliza para letras minúsculas
        
        # Se o texto contiver a exceção, retorna False
        if re.search(self.excecao, texto):
            return False, None

        # Verifica se contém pelo menos um termo do conjunto de padrões
        for p in self.padroes:
            match = re.search(p, texto)
            if match:
                return True, match.group()
        
        return False, None
