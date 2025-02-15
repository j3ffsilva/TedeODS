import importlib
import pytest

@pytest.fixture
def classificador_ods08():
    """Cria uma instância do classificador da ODS 8"""
    modulo = importlib.import_module("classifiers.ods08_classifier")
    return modulo.ODS08Classifier()

# ✅ (E) Testes de Relação "OU" (Combinações de Termos)
@pytest.mark.parametrize(
    "texto, esperado",
    [
        ("produtividade econômica", True),  # Grupo de crescimento econômico
        ("direitos trabalhistas", True),  # Grupo de trabalho decente
        ("pequenas empresas", True),  # Grupo de micro e pequenas empresas
        ("salários iguais", True),  # Grupo de igualdade salarial
        ("turismo sustentável", True),  # Grupo de turismo sustentável
    ]
)
def test_classificador_ods08_ou(texto, esperado, classificador_ods08):
    """Testa diferentes termos do grupo "OU" da ODS08"""
    resultado, _ = classificador_ods08.classify(texto)
    assert resultado == esperado, f"❌ Falha ao classificar: {texto}"

# ✅ (F) Testes com Expressões Regulares (Wildcard `*`)
@pytest.mark.parametrize(
    "texto, esperado",
    [
        ("O microcrédito fortalece pequenos negócios.", True),  # Teste para "microcrédito*"
        ("As microempresas são essenciais para o crescimento econômico.", True),  # Teste para "microempresa*"
        ("A ajuda ao comércio internacional precisa de mais incentivos.", True),  # Teste para "Ajuda ao Comércio"
        ("Compensações de carbono são fundamentais para a sustentabilidade.", False),  # Teste para "compensações de carbono"
    ]
)
def test_classificador_ods08_wildcard(texto, esperado, classificador_ods08):
    """Testa se expressões com wildcard são corretamente classificadas"""
    resultado, _ = classificador_ods08.classify(texto)
    assert resultado == esperado, f"❌ Falha ao classificar wildcard: {texto}"
