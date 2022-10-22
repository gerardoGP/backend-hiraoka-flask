from app import app
from controllers.usuario_controller import UsuarioController
from flask import request


# @app.route("/registro/", methods=['POST'])
# def registrarUsuario():
#     json_input = request.get_json()
#     return UsuarioController().signUp(json_input)

@app.route("/usuario/login", methods=['POST'])
def iniciarSesion():
    json_input = request.get_json()
    return UsuarioController().login(json_input) 

@app.route("/usuario/email/<string:correo>", methods=['GET'])
def busqueda(correo):
    return UsuarioController().buscarEmail(correo)

@app.route("/usuario/id/<int:user_id>",methods=['GET'])
def buscarporId(user_id):
    return UsuarioController.buscarId(user_id)

@app.route("/usuario/lista", methods=['GET'])
def postulantesAll():
    return UsuarioController.listar_usuarios()

@app.route("/usuario/registro", methods=['POST'])
def registrar_usuario():
    json_input = request.get_json()
    return UsuarioController().registro(json_input)

@app.route("/usuario/actualizar", methods=["PUT"])
def actualizar_usuario():
    json_input = request.args
    return UsuarioController().actualizar_usuario(json_input)

@app.route("/usuario/eliminar", methods=["DELETE"])
def eliminar_usuario():
    json_input = request.args
    return UsuarioController().eliminar_usuario(json_input)