from flask import Flask, Blueprint, jsonify, render_template,request,redirect,url_for
from models.ingredientes_db import Ingrediente
from database.db import db

controller_ingredientes = Blueprint('ingredientes', __name__)

@controller_ingredientes.route('/ingredientes', methods=['GET'])
def lista_ingredientes():
    ingredientes = Ingrediente.query.all()
    return render_template('lista_ingredientes.html', ingredientes = ingredientes) 

@controller_ingredientes.route('/ingredientes/ingresar_ingredientes', methods=['GET'])
def volver():
    return render_template('ingresar_ingrediente.html')

@controller_ingredientes.route('/ingresar_ingredientes',methods=['GET'])
def formulario_ingreso():
    return render_template('ingresar_ingrediente.html')

@controller_ingredientes.route('/ingresar_ingredientes',methods=['POST'])
def ingresar_ingrediente():
    nombre = request.form['nombre']
    precio = float(request.form['precio'])
    calorias = int(request.form['kilo calorias'])
    inventario = int(request.form['inventario'])
    es_vegetariano = request.form.get('es_vegetariano','no').lower()=='si'

    db.session.commit()

    nuevo_ingrediente = Ingrediente(
        nombre=nombre,
        precio=precio,
        calorias=calorias,
        inventario=inventario,
        es_vegetariano=es_vegetariano
    )

    db.session.add(nuevo_ingrediente)
    db.session.commit()

    return redirect(url_for('ingredientes.lista_ingredientes'))

