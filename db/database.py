from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

#Variable cadena de conexion:
MARIADB_URL="mysql+pymysql://root:admin@localhost:3315/pyshop_3147246"

#Crear el objeto conexion de la base de datos
engine = create_engine(MARIADB_URL)
#Plantilla base para los modelos
Base = declarative_base()
