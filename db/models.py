from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey

#Crear la clase de modelo(Entidad)
class Categoria(Base):
    __tablename__ = "categorias"
    id = Column(Integer, 
                primary_key=True,
                )
    nombre = Column(String(50))

class Producto(Base):
    __tablename__ = "productos"
    id = Column(Integer, 
                primary_key=True,
                )
    nombre = Column(String(40))
    modelo = Column(String(60))
    precio = Column(Integer)
    id = Column(Integer, 
                 primary_key=True)
    categoria_id = Column (Integer , ForeignKey ("categorias.id"))