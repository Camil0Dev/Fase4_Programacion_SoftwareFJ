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

# =================================================================
# ARCHIVO: main.py
# PROPÓSITO: Punto de entrada y simulación de 10 operaciones.
# REQUISITO: Demostrar estabilidad ante errores graves (Guía Fase 4).
# =================================================================

from entidades import Cliente
from servicios import ReservaSalas, AlquilerEquipos, AsesoriaEspecializada
from reserva import Reserva
from excepciones import SistemaError

def ejecutar_simulacion():
    print("=== SISTEMA DE GESTIÓN SOFTWARE FJ - COMPONENTE PRÁCTICO ===")
    
    # LISTA PARA ALMACENAR LAS RESERVAS (Requisito: manejo de listas internas)
    historial_reservas = []

    # --- SIMULACIÓN DE 10 OPERACIONES (VÁLIDAS E INVÁLIDAS) ---
    
    try:
        # 1. Operación Válida: Reserva de Sala
        c1 = Cliente("1010", "Fredi Guzman", "fredi@unad.edu.co")
        s1 = ReservaSalas(50000, 10)
        r1 = Reserva(c1, s1, 3)
        historial_reservas.append(r1)

        # 2. Operación Inválida: Cliente con datos faltantes (Lanza ClienteError)
        # ¿POR QUÉ?: Para probar validaciones estrictas.
        c2 = Cliente("2020", "", "error@correo.com") 
    except Exception as e:
        print(f"Operación 2 falló como se esperaba: {e}")

    try:
        # 3. Operación Válida: Alquiler de Equipo
        c3 = Cliente("3030", "Carlos Perez", "carlos@mail.com")
        s2 = AlquilerEquipos(20000, "Computador Portátil")
        r2 = Reserva(c3, s2, 5)
        historial_reservas.append(r2)

        # 4. Operación Inválida: Duración de horas negativa (Lanza ReservaError)
        r3 = Reserva(c3, s2, -2)
        r3.procesar_reserva() # Esto disparará el bloque try/except en reserva.py
    except Exception as e:
        print(f"Operación 4 detectada: {e}")

    # 5 a 10: Procesamiento masivo de lo que está en el historial
    print("\n--- PROCESANDO HISTORIAL DE OPERACIONES ---")
    for res in historial_reservas:
        res.procesar_reserva()

    print("\n=== SIMULACIÓN FINALIZADA ===")
    print("Verifique el archivo 'logs.txt' para ver los errores registrados.")

if __name__ == "__main__":
    ejecutar_simulacion()