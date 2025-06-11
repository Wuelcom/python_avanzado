from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
class ejecucion_rutina(Base):
    __tablename__ = "ejecucion_rutina"
    id_ejecucion = Column(Integer, primary_key=True)
    id_rutina = Column(Integer, ForeignKey("rutinas.id_rutina"), nullable=False)