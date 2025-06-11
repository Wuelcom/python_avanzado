from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
class rol_usuarios(Base):
    __tablename__ = "rol_usuarios"
    id_usuario = Column(Integer, primary_key=True)
    id_rol = Column(Integer, ForeignKey("rol_usuarios.id_rol"), nullable=False)
    nombre_usuario = Column(String(50), nullable=False)
    email_usuario = Column(String(100), nullable=False)
    contrasena_usuario = Column(String(100), nullable=False)

