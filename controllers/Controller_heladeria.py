from flask import Flask,Blueprint,request,jsonify,render_template
from database.db import db
from models.ingredientes_db import Ingrediente

controller_es_sano= Blueprint('es_sano',__name__)

@controller_es_sano.route('/es_sano', methods = ['GET'])
def probar_sano():
    try:
        nombre=request.args.get('nombre')

        if not nombre:
            return jsonify({"Por favor proporcione el nombre del ingrediente"}),400
        
        ingrediente = Ingrediente.query.filter_by(nombre=nombre).first()

        if not ingrediente:
            return jsonify({"Este ingrediente no esta en la base de ingredientes"})
        
        sano=Ingrediente.es_sano()

        return jsonify({
            "ingrediente":Ingrediente.nombre,
            "es_sano": sano
        })

    except Exception as e:
        return jsonify({"error:str(e)"})

controller_abastecer = Blueprint('abastecer',__name__)

@controller_abastecer.route('/abastecer', methods=['GET','POST'])
def abastecer():
    if request.method == 'GET':
        return render_template('abastecer.html')
    
    elif request.method == 'POST':
            
            nombre = request.form.get('nombre')
            cantidad = request.form.get('cantidad')

            cantidad=int(cantidad)

            if cantidad <= 0:
                raise ValueError("Debe ser un numero mayor a 0")

    ingrediente= Ingrediente.query.filter_by(nombre=nombre).first()

    if not ingrediente:
        return jsonify({"error":f"Ingrediente '{nombre}' no existe en la base"}),404
    
    ingrediente.abastecer(cantidad)
    db.session.commit()

    return "Ingrediente abastecido"

