# 🔍 Expressões de Busca para Classificação de Trabalhos Acadêmicos nos ODS (PT-BR)

Este diretório contém a versão traduzida e adaptada para o português brasileiro das expressões de busca originalmente desenvolvidas pela Elsevier para apoiar o monitoramento da produção científica relacionada aos [17 ODS da ONU](https://brasil.un.org/pt-br/sdgs).

## 🎯 Contexto e Importância

As expressões foram adaptadas para:

- Capturar a produção científica brasileira sobre sustentabilidade
- Superar limitações de buscas em inglês
- Refletir terminologias específicas do contexto nacional

**Exemplo de adaptação (ODS 6 - Água Potável):**
```sql
(TITLE-ABS-KEY("água potável" OR "abastecimento de água" OR "saneamento básico")
AND NOT ("água mineral" OR "bebidas")  -- Filtro para evitar falsos positivos
)
```

## 📂 Estrutura dos Arquivos

Cada ODS possui um arquivo no formato `ods[NN]_v[X.X].txt` contendo:

1. Metadados da versão
2. Expressões primárias traduzidas
3. Termos expandidos para o contexto brasileiro
4. Filtros de exclusão

## 🏆 Aplicações

| Aplicação | Benefício |
|-----------|-----------|
| Classificação automática | Identificação de trabalhos por ODS em repositórios acadêmicos |
| Análise bibliométrica | Mapeamento da produção científica nacional sobre sustentabilidade |
| Gestão institucional | Subsídio para relatórios de impacto e planejamento estratégico |

## 📌 Dados Originais

Baseado no dataset:
[Elsevier SDGs Mapping v1.1](https://elsevier.digitalcommonsdata.com/datasets/y2zyy9vwzy/1)

## 📄 Autoria e Citação

**Autora principal:**
Dra. Natalia Maria Felix de Souza  
PUC-SP | [nmfsouza@pucsp.br](mailto:nmfsouza@pucsp.br)

**Como citar:**
> SOUZA, Natalia Maria Felix de. **Expressões de busca para classificação de trabalhos acadêmicos nos ODS (PT-BR): tradução e adaptação das expressões originais da Elsevier.** 2024. Disponível em: <https://github.com/j3ffsilva/TedeODS/tree/main/express%C3%B5es_de_busca>. Acesso em: dia mês. ano.


## 📜 Licença
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)