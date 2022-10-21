from app import app
from controllers.marca_controller import MarcaController

@app.route("/marca/lista")
def marcaAll():
    return MarcaController.getAll()