from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
class rutinas(Base):
    __tablename__ = "rutinas"
    id_rutina = Column(Integer, primary_key=True)
    nombre_rutina = Column(String(50), nullable=False)
    descripcion_rutina = Column(String(200), nullable=False)
    fecha_creacion = Column(String(20), nullable=False)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
