# backend/config.py
import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "tu_secreto_aqui")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///password_manager.db")  # Por ejemplo, conexión a una base de datos SQLite


class ProductionConfig(Config):
    DEBUG = False

# back/config.py

class DevelopmentConfig:
    DEBUG = True  # Activa el modo de depuración
    SQLALCHEMY_DATABASE_URI = 'sqlite:///gestor.db'  # Ruta de la base de datos SQLite
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desactiva las notificaciones de cambios para ahorrar recursos
