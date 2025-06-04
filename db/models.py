from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey

#Crear la clase de modelo(Entidad)
class objetivo(Base):
    __tablename__ = "objetivos"
    id_objetivo = Column(Integer, primary_key=True)
    descripcion = Column(String(100), nullable=False, unique=True)

class usuarios (Base):
    __tablename__ = "usuarios"
    id_usuario = Column(Integer, 
                primary_key=True,
                )
    nombre = Column(String(50))
    correo_electronico = Column(String(100), nullable=False, unique=True)
    contraseña = Column(String(100), nullable=False)
    edad = Column(Integer)
    sexo = Column(String(10))
    peso = Column(Integer)
    altura = Column(Integer)
    objetivo_id = Column (Integer , ForeignKey ("objetivos.id_objetivo"))

class poblacion (Base):
    __tablename__ = "poblacion"
    id_usuario = Column(Integer, 
                primary_key=True,
                )
    id_poblacion = Column(Integer, ForeignKey("usuarios.id_usuario"))
    poblacion = Column(String(50)) # e.g., "hombres", "mujeres"
    
class usuarios_comentarios (Base):
    __tablename__ = "usuarios_comentarios"
    id_usuario = Column(Integer, 
                primary_key=True,
                )
    id_comentario = Column(Integer, ForeignKey("comentarios.id_comentario"))
    id_publicacion = Column(Integer, ForeignKey("publicaciones.id_publicacion"))
    comentario = Column(String(200))

class Comentario(Base):
    __tablename__ = "comentarios"
    id_comentario = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"))
    id_publicacion = Column(Integer, ForeignKey("publicaciones.id_publicacion"))
    contenido = Column(String(500))
    fecha = Column(String(20))


class rol_usuarios (Base):
    __tablename__ = "rol_usuarios"
    id_rol = Column(Integer, 
                primary_key=True,
                )
    rol = Column(String(50), nullable=False, unique=True) # e.g., "Administrador", "Usuario", "Entrenador"
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"))

class usuario_rutina (Base):
    __tablename__ = "usuario_rutina"
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), primary_key=True)
    id_rol = Column(Integer, ForeignKey("rol_usuarios.id_rol"), primary_key=True)

class rutinas (Base):
    __tablename__ = "rutinas"
    id_rutinas = Column(Integer, 
                primary_key=True,
                )
    nombre = Column(String(50))
    tipo = Column(String(50)) # e.g., "Fuerza", "Resistencia", "Flexibilidad"
    nivel = Column(String(100)) # e.g., "Principiante", "Intermedio", "Avanzado"
    duracion_minutos = Column(String(15)) 
    descripcion = Column(String(200))
    fecha_inicio = Column(String(20))  
    fecha_fin = Column(String(20))
    creador_id = Column(Integer, ForeignKey("usuarios.id_usuario"))

class ejercicios (Base):
    __tablename__ = "ejercicio"
    id_ejercicio = Column(Integer, 
                primary_key=True,
                )
    nombre = Column(String(50))
    descripcion = Column(String(200))
    video_url = Column(String(200))
    duracion_minutos = Column(String(15))
    id_rutina = Column(Integer, ForeignKey("rutinas.id_rutinas"))


class planes_dieta (Base):
    __tablename__ = "planes_dieta"
    id_dieta  = Column(Integer, 
                primary_key=True,
                )
    nombre_dieta  = Column(String(200))
    descripcion = Column(String(200))
    calorias_aprox = Column(Integer)
    tipo_dieta = Column(String(50)) # e.g., "Vegetariana", "Vegana", "Omnívora"
    creador_id = Column(Integer, ForeignKey("usuarios.id_usuario"))

class progreso_usuario(Base):
    __tablename__ = "progreso_usuarios"
    id_progreso = Column(Integer, primary_key=True)
    fecha_registro = Column(String(20))
    peso_actual = Column(Integer)
    grasa_corporal = Column(Integer)
    masa_muscular = Column(Integer)
    observaciones = Column(String(200))
    imagen_url = Column(String(200))
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"))

class publicaciones(Base):
    __tablename__ = "publicaciones"
    id_publicacion = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"))
    contenido = Column(String(500))
    imagen_url = Column(String(200))
    fecha_publicacion = Column(String(20))

class logros (Base):
    __tablename__ = "logros"
    id_logros   = Column(Integer, 
                primary_key=True,
                )
    id_usuario   = Column(Integer, ForeignKey("usuarios.id_usuario"))
    id_ejecucion   = Column(Integer, ForeignKey("ejecucion_rutina.id_ejecucion"))
    nombre_logro = Column(String(100))
    descripcion = Column(String(200))
    fecha_logro = Column(String(20))
    numero_serie = Column(Integer)
    numero_repeticiones = Column(Integer)
    peso_utilizado = Column(Integer)

class ejecucion_rutina (Base):
    __tablename__ = "ejecucion_rutina"
    id_ejecucion   = Column(Integer, 
                primary_key=True,
                )
    numero_serie = Column(Integer)
    numero_repeticiones = Column(Integer)
    peso_utilizado = Column(Integer)
    id_ejercicio = Column(Integer, ForeignKey("ejercicio.id_ejercicio"))
    id_rutina = Column(Integer, ForeignKey("rutinas.id_rutinas"))

   
