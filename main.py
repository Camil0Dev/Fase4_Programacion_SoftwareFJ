# crear la clase abstracta y obligar el uso de métodos
from abc import ABC, abstractmethod
# registrar la hora exacta en la que ocurre cada error
import datetime

# excepciones para errores
# aquí definimos nuestros propios errores para evitar que el programa colapse

# clase padre para los errores de la empresa
class ErrorSoftwareFJ(Exception):
    """Fallo general del sistema."""
    # pass porque solo necesitamos que herede de Exception
    pass 

# error que vamos a lanzar cuando el usuario deje campos vacíos o ponga formatos raros
class ErrorDatosInvalidos(ErrorSoftwareFJ):
    """Se activa al detectar datos mal ingresados o faltantes."""
    pass 

# error específico para atrapar los problemas al momento de agendar o cancelar algo
class ErrorReserva(ErrorSoftwareFJ):
    """Se activa cuando hay problemas con el estado de las reservas."""
    pass 


# sistema de logs en archivo de texto

# funcion para guardar el historial de errores en un archivo txt
def registrar_error_log(mensaje, tipo_error):
    # variable en None por si el programa falla antes de poder abrir el archivo
    archivo = None 
    try:
        # abrir el archivo en modo (append) para agregar líneas sin borrar lo anterior
        archivo = open("registro_errores.txt", "a")
        
        # fecha y hora actual del sistema para saber cuándo pasó el fallo
        fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # texto exacto que se va a escribir en el bloc de notas
        linea_error = f"[{fecha_hora}] Ocurrió un fallo de tipo ({tipo_error}): {mensaje}\n"
        
        # línea en el archivo txt
        archivo.write(linea_error)
        
    except Exception as e:
        # si algo sale mal y no se puede guardar el txt, lanzamos este print en consola
        print(f"hubo un problema grave intentando guardar el registro del error: {e}")
        
    finally:
        # finally se ejecuta siempre, lo usamos para asegurar que el archivo no quede consumiendo memoria
        if archivo:
            # Cerramos el archivo
            archivo.close()


# clase general

# base de la que van a heredar nuestros clientes y los servicios
class EntidadGeneral(ABC):
    
    # los datos básicos que comparten todas las entidades
    def __init__(self, id_entidad, nombre):
        # guion bajo para indicar que son variables protegidas
        self._id_entidad = id_entidad 
        self._nombre = nombre
    
    # la función de abajo es abstracta
    @abstractmethod
    def mostrar_detalles(self):
        # obligamos a que las clases hijas tengan que programar esta función sí o sí
        pass
