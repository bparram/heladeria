from database.db import db

class Producto(db.Model):
    __tablename__ = 'productos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    precio_publico = db.Column(db.Float, nullable=False)
    malteada_id = db.Column(db.Integer, db.ForeignKey('malteadas.id'), nullable=True)
    copa_id = db.Column(db.Integer, db.ForeignKey('copas.id'),nullable = True)

