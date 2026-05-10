# -------------------------------------------------------------------
# ARCHIVO: excepciones.py
# PROPÓSITO: Definir excepciones personalizadas para "Software FJ".
# REQUISITO: Implementar manejo avanzado de excepciones (Guía Fase 4).
# ----------------------------------------------------------------------

# 1. CLASE MADRE DE EXCEPCIONES
# ¿CÓMO?: Hereda de la clase base 'Exception' de Python.
# ¿POR QUÉ?: Para agrupar todos los errores del sistema bajo un solo tipo.
# ¿PARA QUÉ?: Permite capturar cualquier error del proyecto con un solo bloque.
class SistemaError(Exception):
    """Clase base para todos los errores del sistema Software FJ."""
    pass

# 2. ERROR DE CLIENTE
# ¿CÓMO?: Hereda de 'SistemaError'./Sergio_Bermudez
# ¿POR QUÉ?: La guía pide validaciones robustas y manejo de datos inválidos./Sergio_Bermudez
# ¿PARA QUÉ?: Se lanzará si un cliente tiene datos personales incorrectos o faltantes./Sergio_Bermudez
class ClienteError(SistemaError):
    """Se lanza cuando hay errores en la creación o validación de un Cliente."""
    pass

# 3. ERROR DE SERVICIO
# ¿CÓMO?: Hereda de 'SistemaError'./Sergio_Bermudez
# ¿POR QUÉ?: Requisito de manejar errores por "servicios no disponibles"./Sergio_Bermudez
# ¿PARA QUÉ?: Se usa cuando un servicio (sala, equipo o asesoría) no puede procesarse./Sergio_Bermudez
class ServicioError(SistemaError):
    """Se lanza cuando ocurre un problema con los servicios ofrecidos."""
    pass

# 4. ERROR DE RESERVA/Sergio_Bermudez
# ¿CÓMO?: Hereda de 'SistemaError'./Sergio_Bermudez
# ¿POR QUÉ?: Necesario para gestionar "intentos de reserva incorrectos"./Sergio_Bermudez
# ¿PARA QUÉ?: Se activa si la reserva falla en su confirmación o procesamiento./Sergio_Bermudez
class ReservaError(SistemaError):
    """Se lanza ante fallos en la lógica de reservas, cancelaciones o estados."""
    pass