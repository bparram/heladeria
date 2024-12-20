from database.db import db
from models.funciones import sano

class Ingrediente(db.Model):
    __tablename__ = 'ingredientes'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    calorias = db.Column(db.Integer, nullable=False)
    inventario = db.Column(db.Integer, nullable=False)
    es_vegetariano = db.Column(db.Boolean, nullable=False)

    def es_sano(self):
        return sano(self.calorias,self.vegetariano)
    
    def abastecer(self,cantidad):
        self.inventario += cantidad
