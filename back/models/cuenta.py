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
