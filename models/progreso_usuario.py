from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
class progreso_usuario(Base):
    __tablename__ = "progreso_usuario"
    id_progreso = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    peso_actual = Column(Integer, nullable=False)
    altura_actual = Column(Integer, nullable=False)
    fecha_registro = Column(String(20), nullable=False)
    objetivo = Column(String(100), nullable=False)

