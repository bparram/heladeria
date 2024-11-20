from database.db import db
from models.funciones import Costo_produccion,conteo_calorias,rentabilidad


class Copa(db.Model):
    __tablename__ = 'copas'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    tipo_vaso = db.Column(db.String(50), nullable=False)

    def calcular_costo(self):
        
        precios = [{"precio":ingrediente.precio} for ingrediente in self.ingredientes]
        costoProduccion =Costo_produccion (precios[0],precios[1],precios[2])
        return costoProduccion
    
    def calcular_calorias(self):
        return conteo_calorias([ingrediente.calorias for ingrediente in self.ingredientes])
    
    def calcular_rentabilidad(self):
        precios = [{"precio":ingrediente.precio} for ingrediente in self.ingredientes]
        #valor_produccion = self.calcular_costo()
        return rentabilidad(self.precio_publico,precios[0],precios[1],precios[2])
    

class Copa_Ingrediente(db.Model):
    __tablename__ = 'ingredientes_copas'

    copa_id = db.Column(db.Integer, db.ForeignKey('copas.id'), primary_key=True)
    ingrediente_id = db.Column(db.Integer, db.ForeignKey('ingredientes.id'), primary_key=True)

