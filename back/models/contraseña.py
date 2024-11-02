import hashlib
import base64

class Contraseña:
    def __init__(self, valor):
        self.valor = valor
        self.encriptada = self.cifrar_contraseña()

    def cifrar_contraseña(self):
        cifrado = hashlib.sha256(self.valor.encode()).hexdigest
        return base64.b64encode(cifrado).decode()
    
    def actualizar_contraseña(self, nueva_contraseña):
        self.valor = nueva_contraseña
        self.encriptada = self.cifrar_contraseña()
        
    def verificar_contraseña(self, contraseña_a_verificar):
        return self.cifrar_contraseña() == Contraseña(contraseña_a_verificar).encriptada