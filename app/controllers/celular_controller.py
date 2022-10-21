from app import app,db
from models.celular_model import CelularModel
from schemas.celular_schema import celular_schema, celulares_schema
from marshmallow import ValidationError
from models.usuario_model import UsuarioModel

from flask_jwt_extended import jwt_required

class CelularController:
    def IsEliminado(self, id):
        pass
    
    @jwt_required()
    def getAll():
        celulares = CelularModel.query.all()
        result = celulares_schema.dump(celulares)
        return result,200
    
    @jwt_required()
    def registrar_celular(self, json_input):
        if not json_input:
            return {"message": "No envio datos"}, 400
        try:
            data = celular_schema.load(json_input)
        except ValidationError as err:
            return err.messages, 422
        
        celular = CelularModel(**data)
        db.session.add(celular)
        db.session.commit()
        result = celular_schema.dump(celular)
        return result, 201