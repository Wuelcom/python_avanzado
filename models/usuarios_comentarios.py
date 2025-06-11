from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
class usuarios_comentarios(Base):
    __tablename__ = "usuarios_comentarios"
    id_usuario = Column(Integer, primary_key=True)
    id_comentario = Column(Integer, ForeignKey("comentarios.id_comentario"))
    id_publicacion = Column(Integer, ForeignKey("publicaciones.id_publicacion"))
    comentario = Column(String(200))