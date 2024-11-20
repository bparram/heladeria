from flask import Flask, Blueprint, jsonify, render_template,request,redirect,url_for
from models.ingredientes_db import Ingrediente
from models.copa_db import Copa,Copa_Ingrediente
from models.producto_db import Producto
from database.db import db

controller_copa = Blueprint('crear_copa',__name__)

@controller_copa.route('/crear_copa', methods = ['GET'])
def formulario_creacion():
    return render_template('crear_copa_f.html')

@controller_copa.route('/crear_copa', methods=['POST'])
def crear_copa():
    nombre = request.form['nombre']
    Tipo_vaso = int(request.form['volumen'])
    nombres_ingredientes = request.form['ingredientes'].split(',')

    nombres_ingredientes = [nombre.strip() for nombre in nombres_ingredientes]

    ingredientes = Ingrediente.query.filter(Ingrediente.nombre.in_(nombres_ingredientes)).all()

    nombres_encontrados = [ingrediente.nombre for ingrediente in ingredientes]
    nombres_no_encontrados = list(set(nombres_ingredientes) - set(nombres_encontrados))

    if nombres_no_encontrados:
        return f"Error: Los siguientes ingredientes no existen en la base de datos: {', '.join(nombres_no_encontrados)}", 400

    db.session.commit()

    nueva_malteada = Copa(
        nombre=nombre,
        Tipo_vaso=Tipo_vaso,
        ingredientes=ingredientes
    )

    db.session.add(nueva_malteada)
    db.session.commit()
