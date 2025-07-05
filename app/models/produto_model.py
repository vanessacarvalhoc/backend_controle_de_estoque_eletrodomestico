import sqlite3
from ..database import get_db_connection

class ProdutoModel:
    """
    Modelo que encapsula as operações de banco de dados para produtos.
    """
    @staticmethod
    def get_all():
        """Busca todos os produtos no banco de dados."""
        conn = get_db_connection()
        produtos = conn.execute('SELECT * FROM produtos ORDER BY nome').fetchall()
        conn.close()
        return produtos

    @staticmethod
    def get_by_id(produto_id):
        """Busca um produto pelo seu ID."""
        conn = get_db_connection()
        produto = conn.execute('SELECT * FROM produtos WHERE id = ?', (produto_id,)).fetchone()
        conn.close()
        return produto

    @staticmethod
    def create(data):
        """Cria um novo produto no banco de dados."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO produtos (nome, sku, quantidade, preco) VALUES (?, ?, ?, ?)',
                       (data['nome'], data['sku'], data['quantidade'], data['preco']))
        conn.commit()
        novo_produto_id = cursor.lastrowid
        conn.close()
        return novo_produto_id

    @staticmethod
    def delete(produto_id):
        """Deleta um produto do banco de dados."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM produtos WHERE id = ?', (produto_id,))
        conn.commit()
        rowcount = cursor.rowcount
        conn.close()
        return rowcount > 0

    @staticmethod
    def update_quantidade(produto_id, quantidade):
        """Atualiza a quantidade de um produto."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE produtos SET quantidade = ? WHERE id = ?', (quantidade, produto_id))
        conn.commit()
        rowcount = cursor.rowcount
        conn.close()
        return rowcount > 0
