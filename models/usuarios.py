from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class usuarios(Base):
    __tablename__ = "usuarios"
    id_usuario = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    correo_electronico = Column(String(100), nullable=False, unique=True)
    contraseña = Column(String(100), nullable=False)
    edad = Column(Integer)
    sexo = Column(String(10))
    peso = Column(Integer)
    altura = Column(Integer)
    objetivo_id = Column(Integer, ForeignKey("objetivos.id_objetivo"))