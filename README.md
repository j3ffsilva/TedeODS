# TedeODS - PUC-SP

### Indicadores e rankings internacionais: mapeamento de práticas e reflexões sobre o papel da Universidade nos debates sobre sustentabilidade

## Sobre o Projeto

Universidades como a PUC-SP enfrentam dificuldades para identificar, em seus repositórios de teses e dissertações, os trabalhos que endereçam os Objetivos de Desenvolvimento Sustentável (ODS). O projeto **TedeODS** foi desenvolvido para mitigar esse problema, utilizando técnicas de extração, classificação e disponibilização dos trabalhos acadêmicos de forma acessível.

## Funcionalidades

1. **Extração de Trabalhos Acadêmicos:**
   - Desenvolvimento de um **scraper e parser** para extrair os trabalhos do repositório TEDE da PUC-SP.

2. **Identificação de Trabalhos Relacionados aos ODS:**
   - Utilização de **expressões de busca** baseadas em indexadores acadêmicos como a SciELO.
   - Desenvolvimento de **classificadores** específicos para cada ODS, que associam os abstracts dos trabalhos aos ODS pertinentes.

3. **Disponibilização via API:**
   - Armazenamento estruturado dos trabalhos em um banco de dados.
   - Construção de uma **API RESTful** que permite consulta por:
     - Data
     - Termos específicos
     - Número da ODS associada

4. **Interface Web para Consulta:**
   - Desenvolvimento de um **frontend acessível** para que pesquisadores e público geral possam explorar os trabalhos acadêmicos relacionados às ODS.

## Estrutura do Repositório

```bash
TedeODS/
├── README.md                # Documentação do projeto
├── api/                     # Código da API para consulta dos trabalhos
├── classifiers/             # Classificadores para cada ODS
├── data/                    # Base de dados armazenando os trabalhos
├── expressões_de_busca/     # Expressões usadas para identificar trabalhos ligados às ODS
├── tests/                   # Testes automatizados para os classificadores
├── utils/                   # Utilitários auxiliares para o processamento de dados
├── main.py                  # Arquivo principal do projeto
├── mesclador.ipynb          # Notebook para mesclar e processar os dados
├── requirements.txt         # Dependências do projeto
└── PIPEQ_API_ODS.ipynb      # Notebook para execução da API
```

## Como Executar

### Pré-requisitos
- Python 3.x
- Node.js (para o frontend, se aplicável)
- Banco de Dados (SQLite/PostgreSQL)
- Ambiente virtual Python

### Passos
1. **Clone o repositório:**
   ```sh
   git clone https://github.com/seu_usuario/TedeODS.git
   cd TedeODS
   ```

2. **Crie e ative um ambiente virtual:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows use 'venv\Scripts\activate'
   ```

3. **Instale as dependências:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Execute a API:**
   ```sh
   cd api
   python api.py
   ```

5. **Execute os testes:**
   ```sh
   pytest tests/
   ```

A API será acessível em `http://zumbi:5000/TeseODS`.

## Equipe do Projeto

Este projeto foi desenvolvido pelos seguintes pesquisadores:

- **Dr. Jefferson de Oliveira Silva** | Email: [silvajo@pucsp.br](mailto:silvajo@pucsp.br)
- **Dra. Mariana Ribeiro Jansen Ferreira** | Email: [mrferreira@pucsp.br](mailto:mrferreira@pucsp.br)
- **Dra. Natalia Maria Felix de Souza** | Email: [nmfsouza@pucsp.br](mailto:nmfsouza@pucsp.br)
- **Dra. Terra Friedrich Budini** | Email: [tfbudini@pucsp.br](mailto:tfbudini@pucsp.br)


## Como Citar o Projeto
Se você utilizar o TedeODS em sua pesquisa, por favor cite da seguinte forma:

> SILVA, J. O; FERREIRA, M. R. J.; SOUZA, N. M. F.; BUDINI, T. F. **TedeODS: Indicadores e rankings internacionais: mapeamento de práticas e reflexões sobre o papel da PUC-SP nos debates sobre sustentabilidade**. Disponível em: <https://github.com/j3ffsilva/TedeODS>. Acesso em: [data de acesso].

## Licença
Este projeto está disponível sob a licença **MIT**. Sinta-se à vontade para contribuir e utilizar!

---
*Desenvolvido para facilitar o acesso ao conhecimento acadêmico e promover os Objetivos de Desenvolvimento Sustentável.*