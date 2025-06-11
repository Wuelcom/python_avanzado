from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
class comentarios(Base):
    __tablename__ = "comentarios"
    id_comentario = Column(Integer, primary_key=True)
    id_publicacion = Column(Integer, ForeignKey("publicaciones.id_publicacion"), nullable=False)
    comentario = Column(String(200), nullable=False)
    fecha_comentario = Column(String(20), nullable=False)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)