from app import db,app
from models.marca_model import MarcaModel
from schemas.marca_schema import marca_schema, marcas_schema
from marshmallow import ValidationError
from models.usuario_model import UsuarioModel
from flask_jwt_extended import jwt_required

class MarcaController:
    def IsEliminado(self, id):
        pass
    
    @jwt_required()
    def getAll():
        celulares = MarcaModel.query.all()
        result = marcas_schema.dump(celulares)
        return result,200