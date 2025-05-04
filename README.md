# FURIA Fan Connect

O **FURIA Fan Connect** é uma aplicação interativa criada para coletar dados de fãs da FURIA, uma das maiores organizações de e-sports do mundo. O objetivo do projeto é permitir que fãs se cadastrem, compartilhem informações sobre seus interesses, jogabilidade e interações nas redes sociais, além de permitir o upload de documentos para validação.

## Funcionalidades

- **Cadastro de Dados Pessoais**: Coleta informações como nome, CPF, e-mail, endereço e cidade.
- **Preferências de Jogos**: Permite aos usuários selecionar os jogos que mais jogam (CS, Valorant, LoL, etc.).
- **Interesse por Conteúdo**: O usuário pode informar os tipos de conteúdo que curte, como vídeos, memes, highlights e entrevistas.
- **Feedback**: Opção para os fãs deixarem um feedback sobre a organização FURIA.
- **Upload de Documentos**: Suporta o upload de documentos escaneados (RG ou CPF) com validação via OCR.
- **Validação de Redes Sociais**: Valida os links fornecidos para redes sociais como Instagram, Twitch, Steam e HLTV.
- **Armazenamento de Dados**: Todos os cadastros são armazenados em um arquivo CSV e podem ser visualizados pelos administradores.

## Tecnologias Utilizadas

- **Streamlit**: Framework para criar a interface web interativa.
- **Python**: Linguagem de programação usada para implementar as funcionalidades do backend.
- **OCR (Optical Character Recognition)**: Utilizado para processar e validar documentos de identidade (via `pytesseract`).
- **Pandas**: Biblioteca para manipulação e armazenamento de dados em CSV.
- **APIs de Validação**: Funções customizadas para validar conteúdos nas redes sociais dos usuários.

## Como Rodar o Projeto

### Pré-requisitos

Antes de rodar o projeto, você precisa ter o Python 3.x e as bibliotecas necessárias instaladas. Para instalar as dependências, siga os passos abaixo:

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/furia-fan-connect.git
    cd furia-fan-connect
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

### Rodando a Aplicação

Para rodar o aplicativo Streamlit, execute o comando abaixo:

```bash
streamlit run app/main.py


Estrutura do Projeto
A estrutura do projeto é a seguinte:

graphql
Copiar
Editar
FURIA-Fan-Connect/
│
├── app/
│   ├── main.py            # Arquivo principal da aplicação
│   ├── utils.py           # Funções auxiliares para validação e OCR
│
├── assets/
│   └── furia.jpg          # Imagem do banner
│
├── requirements.txt       # Lista de dependências do projeto
└── fans_data.csv          # Arquivo CSV que armazena os cadastros dos fãs