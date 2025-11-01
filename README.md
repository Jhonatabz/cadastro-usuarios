# Cadastro de Usuários

Este projeto é uma aplicação web para cadastro e autenticação de usuários, desenvolvida com FastAPI, SQLite e Jinja2 Templates.

## Funcionalidades
# Cadastro de Usuários

Aplicação web simples para cadastro e autenticação de usuários construída com FastAPI, SQLite e Jinja2.

Principais funcionalidades
- Cadastro de usuários (com hashing de senha)
- Login / Logout com sessão baseada em cookie
- Interface web com templates Jinja2 (rotas para usuário e administrador)

Stack
- FastAPI
- SQLite
- Jinja2
- passlib (bcrypt) para hashing de senha

Pré-requisitos
- Python 3.10+ (recomendo usar virtualenv/venv)

Instalação (local)
1. Criar e ativar um virtualenv (Windows PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Instalar dependências:

```powershell
pip install -r requirements.txt
```

Como executar

```powershell
python -m uvicorn main:app --reload
```

A aplicação estará disponível em:

http://127.0.0.1:8000

Endpoints principais (web)
- /usuario/login — formulário de login
- /usuario/cadastrar — formulário de cadastro
- /usuario/logout — limpa sessão
- /usuario/profile — página protegida do usuário
- /admin/usuarios — lista de usuários (admin)
- /admin/usuarios/deletar/{id} — excluir usuário (POST)

Observações de segurança
- As senhas são armazenadas com bcrypt via passlib (recomenda-se não usar SHA256 em produção).
- A sessão é gerida com `starlette.middleware.sessions.SessionMiddleware` e requer um `SECRET_KEY`:

    - Em produção, exporte uma variável de ambiente `SECRET_KEY` antes de iniciar a aplicação.

    Exemplo (PowerShell):

    ```powershell
    $env:SECRET_KEY = 'uma-chave-secreta-muito-segura'
    python -m uvicorn main:app --reload
    ```

Testes
- Não há testes automatizados por padrão. Recomendo adicionar testes com pytest + FastAPI TestClient cobrindo cadastro/login/logout e rotas protegidas.

Licença
- MIT
