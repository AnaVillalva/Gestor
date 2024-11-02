# backend/config.py
import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "tu_secreto_aqui")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///password_manager.db")  # Por ejemplo, conexión a una base de datos SQLite

# Puedes crear diferentes configuraciones según el entorno
class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
