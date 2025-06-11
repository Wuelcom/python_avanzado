from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
class logros(Base):
    __tablename__ = "logros"
    id_logro = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    nombre_logro = Column(String(50), nullable=False)
    descripcion_logro = Column(String(200), nullable=False)
    fecha_logro = Column(String(20), nullable=False)
    puntos_logro = Column(Integer, nullable=False)  # Puntos obtenidos por el logro