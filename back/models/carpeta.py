from .cuenta import Cuenta

class Carpeta:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.cuentas = []
    
    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)
    
    def buscar_cuenta(self, nombre_usuario):
        for cuenta in self.cuentas:
            if cuenta.nombre_usuario == nombre_usuario:
                return cuenta
        return None
    
    def eliminar_cuenta(self, nombre_usuario):
        cuenta = self.buscar_cuenta(nombre_usuario)
        if cuenta:
            self.cuentas.remove(cuenta)
            return True
        return False
    
    def listar_cuentas(self):
        return [cuenta.obtener_info()for cuenta in self.cuentas]
    
    def contar_cuentas(self):
        return(len(self.cuentas))
    
# back/models/carpeta.py
from back import db

class Carpeta(db.Model):
    __tablename__ = 'carpetas'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    tipo = db.Column(db.String(80), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    cuentas = db.relationship('Cuenta', backref='carpeta', lazy=True)

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)
        db.session.commit()

