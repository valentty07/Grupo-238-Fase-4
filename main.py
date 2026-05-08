"""
PROGRAMA PRINCIPAL - SISTEMA SOFTWARE FJ
Fase 4 - Demostración de 10 operaciones
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from clases.cliente import Cliente
from clases.servicio import ReservaSalas
from clases.servicios_concretos import AlquilerEquipos, Asesoria
from clases.reserva import Reserva
from clases.logger import GestorLogs
from clases.excepciones import DatosClienteInvalidosException, ParametrosInvalidosException

log = GestorLogs()

print("=" * 70)
print("   SISTEMA INTEGRAL DE GESTIÓN - SOFTWARE FJ")
print("   Demostración de 10 operaciones")
print("=" * 70)

# OPERACIÓN 1: Cliente válido
print("\n1. Crear cliente válido")
try:
    cliente1 = Cliente("Ana López", "ana@email.com", "3105551234", "1234567890")
    print(f"   ✅ Cliente creado: {cliente1.nombre}")
    log.registrar_operacion("Cliente", "ÉXITO", cliente1.nombre)
except Exception as e:
    print(f"   ❌ Error: {e}")

# OPERACIÓN 2: Cliente inválido
print("\n2. Crear cliente inválido (nombre corto)")
try:
    cliente2 = Cliente("An", "test@email.com", "3105551234", "1234567890")
except DatosClienteInvalidosException as e:
    print(f"   ✅ Excepción capturada: {e}")
    log.registrar_error(e, "Cliente inválido")

# OPERACIÓN 3: Servicio ReservaSalas
print("\n3. Crear servicio: Reserva de Sala")
try:
    sala = ReservaSalas("Sala Ejecutiva", "Sala para reuniones", 50000, 10, ["Proyector", "WiFi"])
    print(f"   ✅ Servicio creado: {sala.nombre}")
    log.registrar_operacion("Servicio", "ÉXITO", "ReservaSalas")
except Exception as e:
    print(f"   ❌ Error: {e}")

# OPERACIÓN 4: Servicio AlquilerEquipos
print("\n4. Crear servicio: Alquiler de Equipos")
try:
    equipo = AlquilerEquipos("Laptop Gamer", "Laptop alto rendimiento", 80000, "Computador")
    print(f"   ✅ Servicio creado: {equipo.nombre}")
    log.registrar_operacion("Servicio", "ÉXITO", "AlquilerEquipos")
except Exception as e:
    print(f"   ❌ Error: {e}")

# OPERACIÓN 5: Servicio Asesoria
print("\n5. Crear servicio: Asesoría")
try:
    asesoria = Asesoria("Asesoría Python", "Clases de Python", 120000, "Programación")
    print(f"   ✅ Servicio creado: {asesoria.nombre}")
    log.registrar_operacion("Servicio", "ÉXITO", "Asesoria")
except Exception as e:
    print(f"   ❌ Error: {e}")

# OPERACIÓN 6: Servicio inválido
print("\n6. Crear servicio inválido (precio negativo)")
try:
    sala_invalida = ReservaSalas("Sala Mala", "Precio negativo", -10000, 5)
except ParametrosInvalidosException as e:
    print(f"   ✅ Excepción capturada: {e}")
    log.registrar_error(e, "Servicio inválido")

# OPERACIÓN 7: Reserva válida
print("\n7. Crear reserva válida")
try:
    from datetime import datetime
    # Calcular costo de la sala con 3 horas
    costo_sala = sala.calcular_costo(horas=3)
    print(f"   Costo de sala por 3 horas: ${costo_sala:.2f}")
    
    reserva = Reserva(cliente1, sala, datetime.now(), 3)
    print(f"   ✅ Reserva creada: {reserva.id} - Costo: ${reserva.costo_total:.2f}")
    log.registrar_operacion("Reserva", "ÉXITO", reserva.id)
except Exception as e:
    print(f"   ❌ Error: {e}")
    log.registrar_error(e, "Crear reserva")

# OPERACIÓN 8: Confirmar reserva
print("\n8. Confirmar reserva")
try:
    reserva.confirmar()
    print(f"   ✅ Reserva confirmada. Estado: {reserva.estado}")
    log.registrar_operacion("Confirmar reserva", "ÉXITO", reserva.id)
except Exception as e:
    print(f"   ❌ Error: {e}")
    log.registrar_error(e, "Confirmar reserva")
    
# OPERACIÓN 9: Calcular costo con descuento e impuesto (SOBRECARGA)
print("\n9. Calcular costo con descuento 10% + impuesto 19% (SOBRECARGA)")
try:
    costo = reserva.calcular_costo_total(descuento=10, impuesto=19)
    print(f"   ✅ Costo original: ${reserva.costo_total:.2f}")
    print(f"   ✅ Costo con 10% descuento + 19% impuesto: ${costo:.2f}")
    log.registrar_operacion("Sobrecarga costo", "ÉXITO", f"Descuento 10% + Impuesto 19%")
except Exception as e:
    print(f"   ❌ Error: {e}")

# OPERACIÓN 10: Cancelar reserva
print("\n10. Cancelar reserva")
try:
    reserva.cancelar()
    print(f"   ✅ Reserva cancelada. Estado: {reserva.estado}")
    log.registrar_operacion("Cancelar reserva", "ÉXITO", reserva.id)
except Exception as e:
    print(f"   ❌ Error: {e}")

print("\n" + "=" * 70)
print("   RESUMEN")
print("=" * 70)
print("✅ 10 operaciones completadas")
print("✅ Manejo de excepciones implementado")
print("✅ Sobrecarga de métodos demostrada")
print("✅ Logs guardados en carpeta logs/")
print("=" * 70)