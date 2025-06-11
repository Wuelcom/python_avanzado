from db import Base
from sqlalchemy import Enum, Column, Integer, String, ForeignKey
from models.genero import tipo_genero

class poblacion(Base):
    __tablename__ = "poblacion"
    id_usuario = Column(Integer, primary_key=True)
    id_poblacion = Column(Integer, ForeignKey("usuarios.id_usuario"))
    poblacion = Column(Enum(tipo_genero))  # e.g., "hombres", "mujeres"