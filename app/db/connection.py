import sqlite3

# Conectar ao banco
def conectar():
    return sqlite3.connect("app/db/database.db")

# Criar a tabela
def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        senha TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

# Inserir usuário
def inserir_usuario(nome, email, senha):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)", (nome, email, senha))
    conn.commit()
    conn.close()

# Buscar todos os usuários
def buscar_usuarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios

# Atualizar um usuário
def atualizar_usuario(id, novo_nome, novo_email, nova_senha):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE usuarios SET nome = ?, email = ?, senha = ? WHERE id = ?", (novo_nome, novo_email, nova_senha, id))
    conn.commit()
    conn.close()

# Deletar um usuário
def deletar_usuario(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    conn.commit()
    conn.close()
