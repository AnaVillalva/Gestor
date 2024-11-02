from .contraseña import Contraseña

class Cuenta:
    def __init__(self, nombre_usuario, correo_electronico, cuenta, contraseña):
        self.nombre_usuario = nombre_usuario
        self.correo_electronico = correo_electronico
        self.cuenta = cuenta
        self.contraseña = Contraseña(contraseña)

    def modificar_datos(self, nuevos_datos):
        self.nombre_usuario = nuevos_datos.get("nombre_usuario", self.nombre_usuario)
        self.correo_electronico = nuevos_datos.get("correo_electronico", self.correo_electronico)
        if "contraseña" in nuevos_datos:
            self.contraseña.actualizar_contraseñas(nuevos_datos["contraseña"])

    def obtener_info(self):
        return {
            "nombre_usuario": self.nombre_usuario,
            "correo_electronico": self.correo_electronico,
            "cuenta": self.cuenta,
            "contraseña": self.contraseña.obtener_contraseña()
        }

# back/models/cuenta.py
from back import db

class Cuenta(db.Model):
    __tablename__ = 'cuentas'
    id = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(80), nullable=False)
    correo_electronico = db.Column(db.String(120), nullable=False)
    contraseña = db.Column(db.String(120), nullable=False)
    carpeta_id = db.Column(db.Integer, db.ForeignKey('carpetas.id'), nullable=False)

    def __init__(self, nombre_usuario, correo_electronico, contraseña):
        self.nombre_usuario = nombre_usuario
        self.correo_electronico = correo_electronico
        self.contraseña = contraseña
