# TedeODS - PUC-SP

## Mapeamento de Trabalhos Acadêmicos segundo os Objetivos de Desenvolvimento Sustentável (ODS)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

### Sobre o Projeto

O projeto **TedeODS**, desenvolvido pela PUC-SP, tem como objetivo mapear a produção científica acadêmica de teses e dissertações segundo os **[Objetivos de Desenvolvimento Sustentável (ODS)](https://brasil.un.org/pt-br/sdgs)** da Organização das Nações Unidas (ONU).

A proposta surge diante da dificuldade enfrentada por instituições de ensino superior para identificar, de maneira automatizada e transparente, a aderência de sua produção acadêmica às pautas de sustentabilidade global. O TedeODS propõe uma solução baseada em software de código aberto, modular e escalável, que adota metodologias do **[THE Impact Rankings](https://www.timeshighereducation.com/impactrankings)** para classificação de documentos acadêmicos.

Dados extraídos do repositório institucional **[TEDE PUC-SP](https://tede2.pucsp.br/)**.

---

### Funcionalidades Principais

1. **Extração Automatizada de Trabalhos Acadêmicos**  
   - Ferramentas de *web scraping* e *parsing* para coleta de metadados do TEDE.

2. **Classificação segundo os ODS**  
   - Expressões de busca derivadas do THE Impact Rankings, traduzidas e adaptadas ao português.  
   - Classificadores especializados por ODS aplicados aos resumos dos trabalhos.

3. **API RESTful para Consulta Pública**  
   - Buscas por:  
     - ✅ Ano de publicação  
     - ✅ Termos específicos  
     - ✅ Número/descrição dos ODS  
   - Exemplo de consulta:  
     ```bash
     # Listar trabalhos do ODS 7 (Energia Limpa) publicados em 2022:
     curl "http://localhost:5000/TeseODS?ods=7&ano=2022"
     ```
   - Resposta (JSON):  
     ```json
     {
       "resultados": [
         {
           "titulo": "Energias renováveis no Brasil...",
           "autor": "Fulano et al.",
           "ods": 7,
           "link": "https://tede2.pucsp.br/12345"
         }
       ]
     }
     ```

4. **Interface Web Interativa** *(Em desenvolvimento)*  
   - Dashboard para visualização por:  
     - 📊 Distribuição temporal  
     - 🌍 Mapa de ODS  
     - 🔍 Busca semântica  

---

### Estrutura do Repositório

```bash
TedeODS/
├── api/                     # API Flask (REST)
│   ├── api.py               # Endpoints principais
│   └── database.py          # Conexão com o banco
├── classifiers/             # Modelos de classificação por ODS
├── data/                    # Datasets processados
├── frontend/                # Interface web (React)
├── notebooks/               # Análises exploratórias
│   ├── mesclador.ipynb      
│   └── PIPEQ_API_ODS.ipynb  
└── requirements.txt         # Dependências Python
```

---

## Como Usar

### Pré-requisitos
- Python 3.10+  
- Node.js 16+ (apenas para frontend)  
- Banco de dados PostgreSQL ou SQLite  

### Instalação
```bash
# 1. Clone o repositório
git clone https://github.com/j3ffsilva/TedeODS.git
cd TedeODS

# 2. Configure o ambiente
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Instale dependências
pip install -r requirements.txt

# 4. Configure o banco de dados
cp .env.example .env  # Preencha com suas credenciais
python api/database.py --setup  # Cria tabelas

# 5. Inicie a API
python api/api.py  # Disponível em http://localhost:5000
```

---

## Como Contribuir
1. Abra uma **issue** para discutir mudanças.  
2. Faça um *fork* e envie **pull requests** para a branch `dev`.  
3. Siga os padrões de código (disponíveis em [CONTRIBUTING.md](CONTRIBUTING.md)).  

---

## Equipe
| Nome | Afiliação | Contato |
|------|-----------|---------|
| Dr. Jefferson Silva | PUC-SP/TIDD | [silvajo@pucsp.br](mailto:silvajo@pucsp.br) |
| Dra. Mariana Ferreira | PUC-SP | [mrferreira@pucsp.br](mailto:mrferreira@pucsp.br) |
| Dra. Natalia Maria Felix de Souza | PUC-SP | [nmfsouza@pucsp.br](mailto:nmfsouza@pucsp.br) |
| Dra. Terra Friedrich Budini | PUC-SP | [tfbudini@pucsp.br](mailto:tfbudini@pucsp.br) |

---

## Como Citar o Projeto

Se você utilizar o TedeODS em sua pesquisa, por favor cite-o da seguinte forma:

> SILVA, J. O; FERREIRA, M. R. J.; SOUZA, N. M. F.; BUDINI, T. F. **TedeODS: Indicadores e rankings internacionais: mapeamento de práticas e reflexões sobre o papel da PUC-SP nos debates sobre sustentabilidade**. Disponível em: <https://github.com/j3ffsilva/TedeODS>. Acesso em: [data de acesso].

---

## Licença
Distribuído sob a licença **MIT**. Consulte [LICENSE](LICENSE) para detalhes.
