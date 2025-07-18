import sqlite3
import hashlib

def conectar_usuarios():
    return sqlite3.connect("app/db/usuarios.db")

def criar_tabela_usuarios():
    conn = conectar_usuarios()
    cursor = conn.cursor()
    cursor.execute(f"""
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
    conn = conectar_usuarios()
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

def verificar_login_usuario(email, senha):
    conn = conectar_usuarios()
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

def email_existe(email):
    conn = conectar_usuarios()
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM usuarios WHERE email = ?", (email,))
    existe = cursor.fetchone() is not None
    conn.close()
    return existe

def buscar_usuarios():
    try:
        conn = conectar_usuarios()
        conn.row_factory = sqlite3.Row  # Retorna cada linha como um dicionário
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, email FROM usuarios")
        rows = cursor.fetchall()
        usuarios = [dict(row) for row in rows]
        return usuarios
    finally:
        conn.close()


def atualizar_usuario(id, novo_nome, novo_email, nova_senha):
    conn = conectar_usuarios("usuarios")
    cursor = conn.cursor()
    cursor.execute("UPDATE usuarios SET nome = ?, email = ?, senha = ? WHERE id = ?", (novo_nome, novo_email, nova_senha, id))
    conn.commit()
    conn.close()

def deletar_usuario(id):
    conn = conectar_usuarios("usuarios")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    conn.commit()
    conn.close()


def conectar_admin():
    return sqlite3.connect("app/db/admin.db")

def criar_tabela_admin():
    conn = conectar_admin()
    cursor = conn.cursor()
    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS admin (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        senha_hash TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def inserir_admin(nome, email, senha):
    conn = conectar_admin()
    cursor = conn.cursor()
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()
    try:
        cursor.execute("INSERT INTO admin (nome, email, senha_hash) VALUES (?, ?, ?)", (nome, email, senha_hash))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def verificar_login_admin(email, senha):
    conn = conectar_admin()
    cursor = conn.cursor()

    cursor.execute('SELECT senha_hash FROM admin WHERE email = ?', (email,))
    resultado = cursor.fetchone()

    conn.close()

    if resultado:
        senha_hash = resultado[0]
        senha_informada_hash = hashlib.sha256(senha.encode()).hexdigest()
        if senha_hash == senha_informada_hash:
            return True
    return False