from sqlalchemy import create_engine

#Variable cadena de conexion:
MARIADB_URL="mysql+pymysql://root:admin@localhost:3320/pyshop-3147246"

#Crear el objeto conexion de la base de datos
engine = create_engine(MARIADB_URL)

