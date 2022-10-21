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

class CelularModel(db.Model):
    __tablename__ = 'celulares'
    id = Column(Integer, primary_key=True)
    marca_id = Column(Integer)
    descripcion = Column(String(200))
    codigo = Column(String(20))
    stock = Column(Integer)
    precio_online = Column(Boolean(7,2))
    precio_normal = Column(Boolean(7,2))
    imagen = Column(String(100))