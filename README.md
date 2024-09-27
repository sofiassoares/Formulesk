# Formlesk

## Projeto feito para a disciplina de Programação Web

## Requerimentos

- Python 3
- MySQL

## Configurando o ambiente

Ative o ambiente virtual (caso esteja utilizando):

    source path/to/venv/bin/activate  # Linux/macOS
    path\to\venv\Scripts\activate      # Windows

Instale as dependências do Python com o seguinte comando:

    pip install -r requirements.txt


Configuração das Variáveis de Ambiente

No arquivo config.py altere a seguinte linha para fazer a conexão com o banco de dados:

    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://user:password@host/db'

Substitua de acordo com valores correspondentes no seu ambiente.

e por fim 😁

    flask run
