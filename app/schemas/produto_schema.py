from marshmallow import Schema, fields

class ProdutoSchema(Schema):
    """Define o schema para validação e serialização de produtos."""
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True, error_messages={"required": "O nome é obrigatório."})
    sku = fields.Str(required=True, error_messages={"required": "O SKU é obrigatório."})
    quantidade = fields.Int(required=True, error_messages={"required": "A quantidade é obrigatória."})
    preco = fields.Float(required=True, error_messages={"required": "O preço é obrigatório."})

# Instâncias do schema para um único produto ou uma lista
produto_schema = ProdutoSchema()
produtos_schema = ProdutoSchema(many=True)
