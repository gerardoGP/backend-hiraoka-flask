
from app import app
from controllers.celular_controller import CelularController
from flask import request
@app.route("/celular/lista")
def productoAll():
    return CelularController.getAll()

@app.route("/celular/registrar", methods=["POST"])
def agregar_celular():
    json_input = request.get_json()
    return CelularController().registrar_celular(json_input)