from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
class publicaciones(Base):
    __tablename__ = "publicaciones"
    id_publicacion = Column(Integer, primary_key=True)
    titulo = Column(String(100), nullable=False)
    contenido = Column(String(500), nullable=False)
    fecha_publicacion = Column(String(20), nullable=False)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)

