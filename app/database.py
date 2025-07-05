import sqlite3
import os

DATABASE_PATH = os.path.join(os.path.dirname(__file__), '..', 'estoque.db')

def get_db_connection():
    """Cria uma conexão com o banco de dados SQLite."""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Inicializa o banco de dados e cria a tabela se ela não existir."""
    if os.path.exists(DATABASE_PATH):
        return

    print(f"Banco de dados não encontrado. Criando em: {DATABASE_PATH}")
    conn = get_db_connection()
    
    conn.execute('''
    CREATE TABLE produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        sku TEXT NOT NULL UNIQUE,
        quantidade INTEGER NOT NULL,
        preco REAL NOT NULL
    )
    ''')
    conn.commit()
    conn.close()
    print("Banco de dados e tabela criados com sucesso.")
