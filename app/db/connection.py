import sqlite3
import hashlib

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
        senha_hash TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def inserir_usuario(nome, email, senha):
    conn = conectar()
    cursor = conn.cursor()
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()
    try:
        cursor.execute("INSERT INTO usuarios (nome, email, senha_hash) VALUES (?, ?, ?)", (nome, email, senha_hash))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def verificar_login(email, senha):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('SELECT senha_hash FROM usuarios WHERE email = ?', (email,))
    resultado = cursor.fetchone()

    conn.close()

    if resultado:
        senha_hash = resultado[0]
        senha_informada_hash = hashlib.sha256(senha.encode()).hexdigest()
        if senha_hash == senha_informada_hash:
            return True
    return False

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
