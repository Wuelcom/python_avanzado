from db import Base
from sqlalchemy import Column, Integer, String

class objetivo(Base):
    __tablename__ = "objetivos"
    id_objetivo = Column(Integer, primary_key=True)
    descripcion = Column(String(100), nullable=False, unique=True)