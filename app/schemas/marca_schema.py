from marshmallow import Schema, fields
from helpers.error_helpers import campo_necesario


class MarcaSchema(Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.String()
    

marca_schema = MarcaSchema()
marcas_schema = MarcaSchema(many=True)