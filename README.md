Teste Técnico - API de Cadastro de Empresas e Obrigações Acessórias

Este repositório contém a implementação de um teste técnico para a empresa Dcifre. O objetivo deste projeto é desenvolver uma API RESTful utilizando FastAPI, Pydantic e SQLAlchemy para o cadastro de empresas e a gestão de suas obrigações acessórias perante o governo.
Tecnologias Utilizadas

    FastAPI: Framework moderno e rápido para construir APIs com Python 3.7+ baseado em Python-type hints.
    Pydantic: Utilizado para a validação de dados de entrada e saída, garantindo a integridade dos dados.
    SQLAlchemy: Biblioteca para mapeamento objeto-relacional (ORM) com o banco de dados PostgreSQL.
    PostgreSQL: Sistema de gerenciamento de banco de dados utilizado para armazenar as informações das empresas e obrigações acessórias.
    uvicorn: Servidor ASGI para rodar a aplicação FastAPI.

Funcionalidades da API

A API oferece os seguintes endpoints:

    Cadastro de Empresas
        POST /empresas/: Criação de uma nova empresa no sistema.
        GET /empresas/: Listagem de todas as empresas cadastradas.

    Gestão de Obrigações Acessórias
        POST /obrigacoes/: Criação de uma nova obrigação acessória para uma empresa.
        GET /empresas/{empresa_id}/obrigacoes: Listagem das obrigações acessórias associadas a uma empresa.
    

Como Rodar o Projeto

1. Clonar o repositório:

Clone este repositório para sua máquina local:

git clone https://github.com/fernandooliveira7/teste-tecnico-dcifre.git
cd teste-tecnico-dcifre

2. Criar um ambiente virtual:

Recomendado criar um ambiente virtual para instalar as dependências:

python3 -m venv venv
source venv/bin/activate  # Para sistemas Unix/macOS
venv\Scripts\activate     # Para Windows

3. Instalar as dependências:

Instale as dependências do projeto:

pip install -r requirements.txt

4. Configurar o banco de dados:

Crie o banco de dados dcifre no PostgreSQL:

psql -U postgres
CREATE DATABASE dcifre;
CREATE USER josefernando WITH PASSWORD 'minhasenha';
GRANT ALL PRIVILEGES ON DATABASE dcifre TO josefernando;

5. Rodar as migrações e criar as tabelas:

Execute o script de inicialização para criar as tabelas no banco de dados:

python init_db.py

6. Rodar o servidor:

Para rodar a aplicação, use o Uvicorn:

uvicorn main:app --reload

A API estará disponível em http://127.0.0.1:8000. Você também pode acessar a documentação interativa da API em http://127.0.0.1:8000/docs.


