from sqlalchemy import (
    Column,
    Integer,
    Boolean,
    String,
    Text,
    DateTime,
    func
)
from app import app,db

class UsuarioModel(db.Model):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombres = Column(String(45))
    apellidos = Column(String(45))
    direccion = Column(String(200))
    email = Column(String(320), unique=True)
    password = Column(String(45))