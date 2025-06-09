import sqlite3

def conectar():
    return sqlite3.connect("app/db/database.db")

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        senha TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def inserir_usuario(nome, email, senha):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)", (nome, email, senha))
        conn.commit()
    except sqlite3.IntegrityError:
        return True
    finally:
        conn.close()

def buscar_usuarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios

def atualizar_usuario(id, novo_nome, novo_email, nova_senha):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE usuarios SET nome = ?, email = ?, senha = ? WHERE id = ?", (novo_nome, novo_email, nova_senha, id))
    conn.commit()
    conn.close()

def deletar_usuario(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    conn.commit()
    conn.close()
