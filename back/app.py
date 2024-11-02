# back/app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from back.config import DevelopmentConfig
from back.models.usuario import Usuario
from back.models.carpeta import Carpeta
from back.models.cuenta import Cuenta

# Inicializar la aplicación y la base de datos
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)

# Ruta para registrar un usuario
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    nombre_usuario = data.get("nombre_usuario")
    contraseña_maestra = data.get("contraseña_maestra")

    if Usuario.query.filter_by(nombre_usuario=nombre_usuario).first():
        return jsonify({"error": "El usuario ya existe"}), 400

    usuario = Usuario(nombre_usuario, contraseña_maestra)
    db.session.add(usuario)
    db.session.commit()
    return jsonify({"message": "Usuario registrado exitosamente"}), 201

# Ruta para crear una carpeta
@app.route('/<nombre_usuario>/carpeta', methods=['POST'])
def crear_carpeta(nombre_usuario):
    data = request.json
    nombre_carpeta = data.get("nombre")
    tipo = data.get("tipo", "personal")  # Tipo de carpeta, como "bancaria"

    usuario = Usuario.query.filter_by(nombre_usuario=nombre_usuario).first()
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404

    usuario.crear_carpeta(nombre_carpeta, tipo)
    return jsonify({"message": f"Carpeta '{nombre_carpeta}' creada exitosamente"}), 201

# Ruta para agregar una cuenta a una carpeta
@app.route('/<nombre_usuario>/carpeta/<nombre_carpeta>/cuenta', methods=['POST'])
def agregar_cuenta(nombre_usuario, nombre_carpeta):
    data = request.json
    nombre_usuario_cuenta = data.get("nombre_usuario")
    correo_electronico = data.get("correo_electronico")
    contraseña = data.get("contraseña")

    if not all([nombre_usuario_cuenta, correo_electronico, contraseña]):
        return jsonify({"error": "Faltan datos necesarios"}), 400

    usuario = Usuario.query.filter_by(nombre_usuario=nombre_usuario).first()
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404

    carpeta = Carpeta.query.filter_by(nombre=nombre_carpeta, usuario_id=usuario.id).first()
    if not carpeta:
        return jsonify({"error": "Carpeta no encontrada"}), 404

    nueva_cuenta = Cuenta(nombre_usuario_cuenta, correo_electronico, contraseña)
    carpeta.agregar_cuenta(nueva_cuenta)
    return jsonify({"message": "Cuenta agregada exitosamente"}), 201

# Ruta para listar carpetas de un usuario
@app.route('/<nombre_usuario>/carpetas', methods=['GET'])
def listar_carpetas(nombre_usuario):
    usuario = Usuario.query.filter_by(nombre_usuario=nombre_usuario).first()
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404

    carpetas = [{"nombre": carpeta.nombre, "tipo": carpeta.tipo} for carpeta in usuario.carpetas]
    return jsonify(carpetas), 200

if __name__ == '__main__':
    db.create_all()  # Crea las tablas en la base de datos si no existen
    app.run()

