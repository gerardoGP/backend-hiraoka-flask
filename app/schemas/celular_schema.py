from marshmallow import Schema, fields
from helpers.error_helpers import campo_necesario


class CelularSchema(Schema):
    id = fields.Integer(dump_only=True)
    marca_id = fields.String()
    descripcion = fields.String()
    codigo = fields.String()
    stock = fields.String()
    precio_online = fields.String()    
    precio_normal = fields.Float()
    imagen = fields.String()

celular_schema = CelularSchema()
celulares_schema = CelularSchema(many=True)