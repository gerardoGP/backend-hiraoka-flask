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

class MarcaModel(db.Model):
    __tablename__ = 'marcas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(45))