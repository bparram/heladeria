from database.db import db
from models.funciones import Costo_produccion,conteo_calorias,rentabilidad

class Malteada(db.Model):
    __tablename__ = 'malteadas'

    id = db.Column(db.Integer,primary_key = True)
    nombre_malteada = db.Column(db.Integer, nullable = False)
    volumen = db.Column(db.Integer, nullable=False)

    def calcular_costo(self):
        precios = [{"precio":ingrediente.precio} for ingrediente in self.ingredientes]
        costoProduccion =Costo_produccion (precios[0],precios[1],precios[2])
        return costoProduccion + 500
    
    def calcular_calorias(self):
        return conteo_calorias([ingrediente.calorias for ingrediente in self.ingredientes]) + 200
    
    def calcular_rentabilidad(self):
        precios = [{"precio":ingrediente.precio} for ingrediente in self.ingredientes]
        return rentabilidad(self.precio_publico,precios[0],precios[1],precios[2])


class Malteada_Ingrediente(db.Model):
    __tablename__ = 'ingredientes_malteadas'

    malteada_id = db.Column(db.Integer, db.ForeignKey('malteadas.id'), primary_key=True)
    ingrediente_id = db.Column(db.Integer, db.ForeignKey('ingredientes.id'), primary_key=True)


