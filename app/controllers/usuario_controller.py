from app import db,app
from schemas.usuario_schema import user_schema, users_schema,auth_schema
from models.usuario_model import UsuarioModel
from marshmallow import ValidationError
from flask_jwt_extended import create_access_token,jwt_required,get_jwt_identity

class UsuarioController:
    def buscarId(id):
        usuario = UsuarioModel().query.filter_by(id=id)
        result = users_schema.dump(usuario)
        return result,200
    
    def buscarEmail(self,email):
        usuario = UsuarioModel().query.filter_by(email=email)
        result = users_schema.dump(usuario)
        return result,200
    
    def __searchUser(self, email):
        usuario = UsuarioModel().query.filter_by(email=email).first()
        return usuario
    
    def login(self, json_input):
        data = auth_schema.load(json_input)
        user = self.__searchUser(data['email'])
        if not user:
            return {"message":"Correo no encontrado"},400
        #access_token = create_access_token(identity=user.id, name=user.nombres)
        access_token = create_access_token(identity=user.nombres)
        return {"access_token": access_token}, 200
    
    def registro(self, json_input):
        #validamos que los datos enviados no esten vacios
        if not json_input:
            return {"message":"No ha enviado datos de entrada."},400
        try:
            #validamos que no exista el usuario
            data = user_schema.load(json_input)
        except ValidationError as err:
            return err.messages,422
        
        user = self.__searchUser(data["email"])
        if not user:
            #no esta registrado
            usuario = UsuarioModel(**data)
            db.session.add(usuario)
            db.session.commit()
            result = user_schema.dump(usuario)
            return result,201
        
        return {"message":"Error, el usuario ya existe, no puede haber duplicado"},400
    
    @jwt_required()
    def actualizar_usuario(self, json_input):
        id = json_input.get("id")
        usuario = UsuarioModel().query.get(id)
        usuario.nombres = json_input.get("nombres")
        usuario.apellidos = json_input.get("apellidos")
        usuario.direccion = json_input.get("direccion")
        db.session.commit()
        result = user_schema.dump(usuario)
        return {"message":"Actualizado correctamente","content":result}, 200
    

    def eliminar_usuario(self, json_input):
        id = json_input.get("id")
        usuario = UsuarioModel().query.get(id)
        if not usuario:
            return{
                "message":"No se puede eliminar, el usuario no existe",
                "id":id
                },400
        db.session.delete(usuario)
        db.session.commit()
        return {"message":"Eliminado Correctamente"}
    
    @jwt_required()
    def listar_usuarios():
        usuarios = UsuarioModel().query.all()
        result = users_schema.dump(usuarios)
        return result,200