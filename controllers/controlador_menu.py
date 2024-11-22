from flask import Flask, Blueprint, jsonify, render_template
from models.ingredientes_db import Ingrediente
from models.producto_db import Producto

traer_menu = Blueprint('controlador', __name__)


@traer_menu.route('/menu', methods=['GET'])
def mostrar_menu():
    productos = Producto.query.all()
    return render_template('menu.html', productos=productos)









