from abc import ABC, abstractmethod
from excepciones import ClienteError 

# 1. CLASE ABSTRACTA (Entidad General)
# ¿CÓMO?: Usamos ABC (Abstract Base Classes).
# ¿POR QUÉ?: La guía pide una clase abstracta para entidades generales.
# ¿PARA QUÉ?: Asegura que cualquier entidad tenga una identificación básica.
class EntidadSistema(ABC):
    def __init__(self, id_entidad):
        self.id_entidad = id_entidad

    @abstractmethod
    def mostrar_informacion(self):
        pass

# =================================================================
# CLASE: Cliente
# ¿CÓMO?: Implementa encapsulación (__nombre, __email) y herencia.
# ¿POR QUÉ?: Protege los datos y cumple con los requisitos de la Fase 4.
# ¿PARA QUÉ?: Gestiona la información de quien realiza la reserva.
# =================================================================
class Cliente(EntidadSistema):
    def __init__(self, id_entidad, nombre, email):
        super().__init__(id_entidad)
        # Validación de datos para evitar errores en el sistema
        if not nombre or not email:
            raise ClienteError("El nombre y el email son obligatorios.")
        self.__nombre = nombre
        self.__email = email

    def mostrar_informacion(self):
        return f"Cliente: {self.__nombre} | ID: {self.id_entidad}"

    # Getters para acceder a los atributos privados
    def get_nombre(self):
        return self.__nombre

    def get_email(self):
        return self.__email