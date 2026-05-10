#-------------------------------------------------------------------------------
# ARCHIVO: reserva.py/Sergio_Bermudez
# PROPÓSITO: Gestionar la unión entre Clientes y Servicios./Sergio_Bermudez
# REQUISITO: Uso de try/except/else/finally y registro de logs./Sergio_Bermudez
# --------------------------------------------------------------------------------

from excepciones import ReservaError, ServicioError
import datetime

class Reserva:
    def __init__(self, cliente, servicio, duracion_horas):
        """
        ¿CÓMO?: Recibe objetos de Cliente y Servicio./Sergio_Bermudez
        ¿POR QUÉ?: Para integrar los componentes del sistema (Software FJ)./Sergio_Bermudez
        ¿PARA QUÉ?: Centraliza la operación de venta o alquiler./Sergio_Bermudez
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
            # 1. VALIDACIÓN (Posible error)/Sergio_Bermudez
            if self.duracion_horas <= 0:
                raise ReservaError("La duración debe ser mayor a 0 horas.")
            
            # 2. CÁLCULO (Uso de polimorfismo del servicio)/Sergio_Bermudez
            costo_total = self.servicio.calcular_costo() * self.duracion_horas
            
        except (ReservaError, ServicioError) as e:
            # ¿QUÉ HACE?: Captura errores específicos de nuestra lógica./Sergio_Bermudez
            self.estado = "Fallida"
            mensaje_error = f"[ERROR LOG] {datetime.datetime.now()} - {type(e).__name__}: {e}"
            print(mensaje_error)
            
            # REGISTRO EN LOGS (Requisito: "Cada error debe registrarse en un archivo")/Sergio_Bermudez
            with open("logs.txt", "a") as f:
                f.write(mensaje_error + "\n")
                
        except Exception as e:
            # ¿QUÉ HACE?: Captura cualquier otro error inesperado./Sergio_Bermudez
            print(f"Ocurrió un error no previsto: {e}")
            
        else:
            # ¿QUÉ HACE?: Se ejecuta SOLO si no hubo errores en el bloque 'try'./Sergio_Bermudez
            self.estado = "Confirmada"
            print(f"Reserva exitosa: {self.servicio.obtener_detalle()}")
            print(f"Total a pagar: ${costo_total}")
            
        finally:
            # ¿QUÉ HACE?: Se ejecuta SIEMPRE (haya error o no)./Sergio_Bermudez
            # ¿PARA QUÉ?: Para confirmar que el sistema sigue activo./Sergio_Bermudez
            print(f"Estado final de la operación: {self.estado}")
            print("Sistema de Software FJ listo para la siguiente operación.")