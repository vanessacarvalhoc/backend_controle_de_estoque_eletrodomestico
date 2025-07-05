from flask import Blueprint, request, jsonify, send_from_directory
from marshmallow import ValidationError
from .schemas.produto_schema import produto_schema, produtos_schema
from .models.produto_model import ProdutoModel
import sqlite3

# Cria um Blueprint para agrupar as rotas
bp = Blueprint('routes', __name__)

@bp.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@bp.route('/buscar_produtos', methods=['GET'])
def get_produtos():
    """Retorna a lista de todos os produtos."""
    todos_produtos = ProdutoModel.get_all()
    result = produtos_schema.dump(todos_produtos)
    return jsonify(result)

@bp.route('/adicionar_produto', methods=['POST'])
def add_produto():
    """Adiciona um novo produto."""
    json_data = request.get_json()
    if not json_data:
        return jsonify({"error": "Nenhum dado de entrada fornecido"}), 400

    try:
        data = produto_schema.load(json_data)
        novo_produto_id = ProdutoModel.create(data)
        novo_produto = {"id": novo_produto_id, **data}
        return jsonify(produto_schema.dump(novo_produto)), 201
    except ValidationError as err:
        return jsonify(err.messages), 422
    except sqlite3.IntegrityError:
        return jsonify({"error": {"sku": ["SKU já existe no banco de dados."]}}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/deletar_produto/<int:produto_id>', methods=['DELETE'])
def delete_produto(produto_id):
    """Deleta um produto pelo seu ID."""
    if ProdutoModel.delete(produto_id):
        return jsonify({"success": True, "message": "Produto removido com sucesso"}), 200
    return jsonify({"error": "Produto não encontrado"}), 404

@bp.route('/vender_produto/<int:produto_id>/vender', methods=['POST'])
def vender_produto(produto_id):
    """Vende uma quantidade de um produto."""
    data = request.json
    try:
        quantidade = int(data.get('quantidade'))
        if quantidade <= 0: raise ValueError()
    except (ValueError, TypeError):
        return jsonify({"error": "Quantidade inválida"}), 400
    
    produto = ProdutoModel.get_by_id(produto_id)
    if not produto:
        return jsonify({"error": "Produto não encontrado"}), 404
    
    if produto['quantidade'] < quantidade:
        return jsonify({"error": "Estoque insuficiente"}), 400

    nova_quantidade = produto['quantidade'] - quantidade
    ProdutoModel.update_quantidade(produto_id, nova_quantidade)
    
    produto_atualizado = ProdutoModel.get_by_id(produto_id)
    return jsonify(produto_schema.dump(produto_atualizado)), 200

@bp.route('/adicionar_estoque_produto/<int:produto_id>', methods=['POST'])
def add_estoque(produto_id):
    """Adiciona estoque a um produto."""
    data = request.json
    try:
        add_quantidade = int(data.get('quantidade'))
        if add_quantidade <= 0: raise ValueError()
    except (ValueError, TypeError):
        return jsonify({"error": "Quantidade inválida"}), 400

    produto = ProdutoModel.get_by_id(produto_id)
    if not produto:
        return jsonify({"error": "Produto não encontrado"}), 404

    nova_quantidade = produto['quantidade'] + add_quantidade
    ProdutoModel.update_quantidade(produto_id, nova_quantidade)
    
    updated_produto = ProdutoModel.get_by_id(produto_id)
    return jsonify(produto_schema.dump(updated_produto)), 200
