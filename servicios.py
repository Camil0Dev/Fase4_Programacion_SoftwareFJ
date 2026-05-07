# =================================================================
# ARCHIVO: servicios.py
# PROPÓSITO: Definir la jerarquía de servicios de Software FJ.
# REQUISITO: Clases abstractas, herencia y polimorfismo (Guía Fase 4).
# =================================================================

from abc import ABC, abstractmethod
from excepciones import ServicioError  # Importamos el error personalizado

# 1. CLASE ABSTRACTA SERVICIO
# ¿CÓMO?: Hereda de ABC para definir métodos que las hijas DEBEN tener.
# ¿POR QUÉ?: La guía pide una clase abstracta para servicios especializados.
# ¿PARA QUÉ?: Garantiza que todo servicio tenga costo y descripción.
class Servicio(ABC):
    def __init__(self, nombre_servicio, costo_base):
        self.nombre_servicio = nombre_servicio
        self.costo_base = costo_base

    @abstractmethod
    def calcular_costo(self):
        """Método abstracto para el cálculo de costos según el tipo."""
        pass

    @abstractmethod
    def obtener_detalle(self):
        """Método abstracto para la descripción del servicio."""
        pass

# 2. SERVICIO: RESERVA DE SALAS (Herencia)
# ¿CÓMO?: Clase hija que sobrescribe los métodos abstractos.
# ¿POR QUÉ?: Implementa el polimorfismo requerido por la actividad.
class ReservaSalas(Servicio):
    def __init__(self, costo_base, capacidad):
        super().__init__("Reserva de Salas", costo_base)
        self.capacidad = capacidad

    def calcular_costo(self):
        # Polimorfismo: cálculo específico para salas
        return self.costo_base * 1.10  # Ejemplo: 10% adicional por mantenimiento

    def obtener_detalle(self):
        return f"{self.nombre_servicio} para {self.capacidad} personas."

# 3. SERVICIO: ALQUILER DE EQUIPOS (Herencia)
class AlquilerEquipos(Servicio):
    def __init__(self, costo_base, tipo_equipo):
        super().__init__("Alquiler de Equipos", costo_base)
        self.tipo_equipo = tipo_equipo

    def calcular_costo(self):
        return self.costo_base # Costo fijo por equipo

    def obtener_detalle(self):
        return f"{self.nombre_servicio}: {self.tipo_equipo}."

# 4. SERVICIO: ASESORÍAS (Herencia y validación)
class AsesoriaEspecializada(Servicio):
    def __init__(self, costo_base, especialidad):
        # VALIDACIÓN ROBUSTA (Requisito de la guía)
        if not especialidad:
            raise ServicioError("Debe indicar la especialidad de la asesoría.")
        
        super().__init__("Asesoría Especializada", costo_base)
        self.especialidad = especialidad

    def calcular_costo(self):
        return self.costo_base * 1.50 # Las asesorías tienen un recargo del 50%

    def obtener_detalle(self):
        return f"{self.nombre_servicio} en {self.especialidad}."