from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
class planes_dieta(Base):
    __tablename__ = "planes_dieta"
    id_plan = Column(Integer, primary_key=True)
    nombre_plan = Column(String(50), nullable=False)
    descripcion_plan = Column(String(200), nullable=False)
    fecha_creacion = Column(String(20), nullable=False)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)