# =================================================================
# ARCHIVO: reserva.py
# PROPÓSITO: Gestionar la unión entre Clientes y Servicios.
# REQUISITO: Uso de try/except/else/finally y registro de logs.
# =================================================================

from excepciones import ReservaError, ServicioError
import datetime

class Reserva:
    def __init__(self, cliente, servicio, duracion_horas):
        """
        ¿CÓMO?: Recibe objetos de Cliente y Servicio.
        ¿POR QUÉ?: Para integrar los componentes del sistema (Software FJ).
        ¿PARA QUÉ?: Centraliza la operación de venta o alquiler.
        """
        self.cliente = cliente
        self.servicio = servicio
        self.duracion_horas = duracion_horas
        self.fecha_creacion = datetime.datetime.now()
        self.estado = "Pendiente"

    def procesar_reserva(self):
        """
        ¿CÓMO?: Implementa bloques try/except/else/finally detallados.
        ¿POR QUÉ?: Requisito de la Fase 4 para garantizar estabilidad.
        """
        print(f"\n--- Iniciando proceso de reserva para: {self.cliente.nombre} ---")
        
        try:
            # 1. VALIDACIÓN (Posible error)
            if self.duracion_horas <= 0:
                raise ReservaError("La duración debe ser mayor a 0 horas.")
            
            # 2. CÁLCULO (Uso de polimorfismo del servicio)
            costo_total = self.servicio.calcular_costo() * self.duracion_horas
            
        except (ReservaError, ServicioError) as e:
            # ¿QUÉ HACE?: Captura errores específicos de nuestra lógica.
            self.estado = "Fallida"
            mensaje_error = f"[ERROR LOG] {datetime.datetime.now()} - {type(e).__name__}: {e}"
            print(mensaje_error)
            
            # REGISTRO EN LOGS (Requisito: "Cada error debe registrarse en un archivo")
            with open("logs.txt", "a") as f:
                f.write(mensaje_error + "\n")
                
        except Exception as e:
            # ¿QUÉ HACE?: Captura cualquier otro error inesperado.
            print(f"Ocurrió un error no previsto: {e}")
            
        else:
            # ¿QUÉ HACE?: Se ejecuta SOLO si no hubo errores en el bloque 'try'.
            self.estado = "Confirmada"
            print(f"Reserva exitosa: {self.servicio.obtener_detalle()}")
            print(f"Total a pagar: ${costo_total}")
            
        finally:
            # ¿QUÉ HACE?: Se ejecuta SIEMPRE (haya error o no).
            # ¿PARA QUÉ?: Para confirmar que el sistema sigue activo.
            print(f"Estado final de la operación: {self.estado}")
            print("Sistema de Software FJ listo para la siguiente operación.")