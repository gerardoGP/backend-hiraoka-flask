from marshmallow import Schema, fields
from helpers.error_helpers import campo_necesario


class UsuarioSchema(Schema):
    id = fields.Integer(dump_only=True)
    nombres = fields.String(validate=campo_necesario)
    apellidos = fields.String(validate=campo_necesario)
    direccion = fields.String(validate=campo_necesario)
    email = fields.String(validate=campo_necesario)
    password = fields.String(validate=campo_necesario)    

user_schema = UsuarioSchema()
users_schema = UsuarioSchema(many=True)

class AutenticacionSchema(Schema):
    #suarioPassword = fields.String(required=True, validate=campo_necesario)
    email = fields.String(required=True, validate=campo_necesario)

auth_schema = AutenticacionSchema()