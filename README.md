# Cadastro de Usuários

Este projeto é uma aplicação web para cadastro e autenticação de usuários, desenvolvida com FastAPI, SQLite e Jinja2 Templates.

## Funcionalidades

- Cadastro de novos usuários
- Login de usuários
- Validação de email único
- Hash de senha para segurança
- Interface web com templates HTML

## Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLite](https://www.sqlite.org/index.html)
- [Jinja2](https://jinja.palletsprojects.com/)
- [Pydantic](https://docs.pydantic.dev/)

## Estrutura do Projeto

app/ 
    ├── db/ # Conexão e operações com o banco de dados 
    ├── models/ # Modelos Pydantic 
    ├── routes/ # Rotas da aplicação 
    └── templates/ # Templates HTML

## Como Executar

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/cadastro-usuarios.git
    cd cadastro-usuarios
    ```

2. Instale as dependências:
    ```bash
    pip install fastapi uvicorn jinja2
    ```

3. Execute a aplicação:
    ```bash
    uvicorn app.main:app --reload
    ```

4. Acesse no navegador:
    ```
    http://localhost:8000/usuario/login
    ```

## Observações

- As senhas são armazenadas de forma segura (hash SHA-256).
- O projeto pode ser expandido para incluir autenticação por sessão ou JWT.

## Licença

Este projeto está sob a licença MIT.