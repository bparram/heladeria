from flask import Flask, Blueprint, jsonify, render_template,request,redirect,url_for
from models.ingredientes_db import Ingrediente
from models.malteada_db import Malteada,Malteada_Ingrediente
from models.producto_db import Producto
from database.db import db

controller_malteada = Blueprint('crear_malteada',__name__)

@controller_malteada.route('/crear_malteada', methods = ['GET'])
def formulario_creacion():
    return render_template('crear_malteada_f.html')

@controller_malteada.route('/crear_malteada', methods=['POST'])
def crear_malteada():
    nombre = request.form['nombre']
    volumen = int(request.form['volumen'])
    nombres_ingredientes = request.form['ingredientes'].split(',')

    nombres_ingredientes = [nombre.strip() for nombre in nombres_ingredientes]

    ingredientes = Ingrediente.query.filter(Ingrediente.nombre.in_(nombres_ingredientes)).all()

    nombres_encontrados = [ingrediente.nombre for ingrediente in ingredientes]
    nombres_no_encontrados = list(set(nombres_ingredientes) - set(nombres_encontrados))

    if nombres_no_encontrados:
        return f"Error: Los siguientes ingredientes no existen en la base de datos: {', '.join(nombres_no_encontrados)}", 400

    db.session.commit()

    nueva_malteada = Malteada(
        nombre=nombre,
        volumen=volumen,
        ingredientes=ingredientes
    )

    db.session.add(nueva_malteada)
    db.session.commit()

    return redirect(url_for('controller_malteada.lista_malteadas'))