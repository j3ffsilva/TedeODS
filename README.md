# TedeODS

### Identificação de Trabalhos Acadêmicos Relacionados aos ODS no Repositório da PUC-SP

## Sobre o Projeto

Universidades como a PUC-SP enfrentam dificuldades para identificar, em seus repositórios de teses e dissertações, os trabalhos que endereçam os Objetivos de Desenvolvimento Sustentável (ODS). O projeto **TedeODS** foi desenvolvido para mitigar esse problema, utilizando técnicas de extração, classificação e disponibilização dos trabalhos acadêmicos de forma acessível.

## Funcionalidades

1. **Extração de Trabalhos Acadêmicos:**
   - Foi desenvolvido um **scraper e parser** para extrair todos os trabalhos do repositório TEDE da PUC-SP.

2. **Identificação de Trabalhos Relacionados aos ODS:**
   - Utilização de **expressões de busca** baseadas em indexadores acadêmicos como a SciELO.
   - Desenvolvimento de um **classificador** para associar os abstracts dos trabalhos às ODS.

3. **Disponibilização via API:**
   - Armazenamento dos trabalhos em um banco de dados estruturado.
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
├── data/                    # Base de dados armazenando os trabalhos
├── expressões_de_busca/     # Expressões usadas para identificar trabalhos ligados às ODS
├── frontend/                 # Código do frontend para consulta pública
└── parser/                   # Scripts para extração e processamento de dados
```

## Como Executar

### Pré-requisitos
- Python 3.x
- Node.js (para o frontend)
- Banco de Dados (SQLite/PostgreSQL)

### Passos
1. **Clone o repositório:**
   ```sh
   git clone https://github.com/seu_usuario/TedeODS.git
   cd TedeODS
   ```

2. **Instale as dependências da API:**
   ```sh
   cd api
   pip install -r requirements.txt
   ```

3. **Execute a API:**
   ```sh
   python app.py
   ```

4. **Instale e execute o frontend:**
   ```sh
   cd ../frontend
   npm install
   npm start
   ```

A API será acessível em `http://zumbi:5000/TeseODS` e o frontend em `https://projectods.netlify.app/`.

## Equipe do Projeto

Este projeto foi desenvolvido pelos seguintes pesquisadores:

- **Dra. Terra Friedrich Budini** | Email: [tfbudini@pucsp.br](mailto:tfbudini@pucsp.br)
- **Dra. Natalia Maria Felix de Souza** | Email: [nmfsouza@pucsp.br](mailto:nmfsouza@pucsp.br)
- **Dra. Mariana Ribeiro Jansen Ferreira** | Email: [mrferreira@pucsp.br](mailto:mrferreira@pucsp.br)
- **Dr. Jefferson de Oliveira Silva** | Email: [silvajo@pucsp.br](mailto:silvajo@pucsp.br)

## Licença
Este projeto está disponível sob a licença **MIT**. Sinta-se à vontade para contribuir e utilizar!

---
*Desenvolvido para facilitar o acesso ao conhecimento acadêmico e promover os Objetivos de Desenvolvimento Sustentável.*
