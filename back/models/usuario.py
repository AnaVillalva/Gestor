from werkzeug.security import generate_password_hash, check_password_hash
from .carpeta import Carpeta

class Usuario:
    def __init__(self, nombre_usuario, contraseña_maestra):
        self.nombre_usuario = nombre_usuario
        self.contraseña_maestra = generate_password_hash(contraseña_maestra)
        self.carpetas = []
    
    def verificar_contraseña_maestra(self, contraseña):
        return check_password_hash(self.contraseña_maestra, contraseña)

    def crear_carpeta(self, nombre, tipo):
        nueva_carpeta = Carpeta(nombre, tipo)
        self.carpetas.append(nueva_carpeta)
    
    def buscar_carpeta(self, nombre):
        for carpeta in self.carpetas:
            if carpeta.nombre == nombre:
                return carpeta
        return None
    
    def eliminar_carpeta(self, nombre):
        carpeta= self.buscar_carpeta(nombre)
        if carpeta:
            self.carpetas.remove(carpeta)
            return True
        return False
    
    def agregar_cuenta_a_carpeta(self, nombre_carpeta, cuenta):
        carpeta = self.buscar_carpeta(nombre_carpeta)
        if carpeta:
            carpeta.agregar_cuenta(cuenta)
            return True
        return False
    
    def buscar_cuenta(self, nombre_carpeta, nombre_usuario):
        carpeta= self.buscar_carpeta(nombre_carpeta)
        if carpeta:
            return carpeta.buscar_cuenta(nombre_usuario)
        return None
    
    def modificar_cuenta(self, nombre_carpeta, nombre_usuario, nuevos_datos):
        cuenta = self.buscar_carpeta(nombre_carpeta, nombre_usuario)
        if cuenta:
            cuenta.nombre_usuario = nuevos_datos.get("nombre_usuario", cuenta.nombre_usuario)
            cuenta.correo_electronico = nuevos_datos.get("ncorreo_electronico", cuenta.nombre_usuario)
            if "contraseña" in nuevos_datos:
                cuenta.contraseña.actualizar_contraseña(nuevos_datos["contraseña"])
            return True
        return False
    
    def eliminar_cuenta(self, nombre_carpeta, nombre_usuario):
        carpeta = self.buscar_carpeta(nombre_carpeta)
        if carpeta:
            return carpeta.eliminar_cuenta(nombre_usuario)
        return False
