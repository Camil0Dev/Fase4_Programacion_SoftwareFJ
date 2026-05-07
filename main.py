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