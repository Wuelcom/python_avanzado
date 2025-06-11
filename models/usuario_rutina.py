from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
class usuario_rutina(Base):
    __tablename__ = "rutina_usuario"
    id_usuario = Column(Integer, primary_key=True)
    id_rutina = Column(Integer, ForeignKey("rutinas.id_rutina"), nullable=False)
    nombre_usuario = Column(String(50), nullable=False)
    email_usuario = Column(String(100), nullable=False)
    contrasena_usuario = Column(String(100), nullable=False)