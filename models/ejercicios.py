from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
class ejercicios(Base):
    __tablename__ = "ejercicios"
    id_ejercicio = Column(Integer, primary_key=True)
    nombre_ejercicio = Column(String(100), nullable=False)
    descripcion_ejercicio = Column(String(500), nullable=False)
    fecha_creacion = Column(String(20), nullable=False)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    
