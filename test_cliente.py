"""
PRUEBA DE LA CLASE CLIENTE
Estudiante 1 - Verificar que todo funciona correctamente
"""

from clases.cliente import Cliente
from clases.excepciones import DatosClienteInvalidosException

print("=" * 60)
print("PRUEBA DE CLASE CLIENTE - SISTEMA SOFTWARE FJ")
print("=" * 60)

# ========== PRUEBA 1: CREAR CLIENTE VÁLIDO ==========
print("\n✅ PRUEBA 1: Crear cliente válido")
try:
    cliente1 = Cliente(
        nombre="Ana Rodríguez",
        email="ana.rodriguez@email.com",
        telefono="3105551234",
        identificacion="1234567890"
    )
    print(cliente1.mostrar_informacion("completo"))
    print("✅ Cliente creado exitosamente")
except Exception as e:
    print(f"❌ Error: {e}")

# ========== PRUEBA 2: CREAR CLIENTE CON NOMBRE CORTO ==========
print("\n❌ PRUEBA 2: Crear cliente con nombre muy corto (debe fallar)")
try:
    cliente2 = Cliente(
        nombre="An",
        email="test@email.com",
        telefono="3105551234",
        identificacion="1234567890"
    )
    print(cliente2.mostrar_informacion("completo"))
except DatosClienteInvalidosException as e:
    print(f"✅ Excepción capturada correctamente: {e}")

# ========== PRUEBA 3: CREAR CLIENTE CON EMAIL INVÁLIDO ==========
print("\n❌ PRUEBA 3: Crear cliente con email inválido (debe fallar)")
try:
    cliente3 = Cliente(
        nombre="Carlos Pérez",
        email="carlos.email-invalido",
        telefono="3105551234",
        identificacion="1234567890"
    )
    print(cliente3.mostrar_informacion("completo"))
except DatosClienteInvalidosException as e:
    print(f"✅ Excepción capturada correctamente: {e}")

# ========== PRUEBA 4: MODIFICAR CLIENTE EXISTENTE ==========
print("\n✅ PRUEBA 4: Modificar datos de cliente existente")
try:
    print(f"Antes: {cliente1.nombre}")
    cliente1.nombre = "Ana María Rodríguez Gómez"
    print(f"Después: {cliente1.nombre}")
    print("✅ Nombre actualizado correctamente")
except Exception as e:
    print(f"❌ Error: {e}")

# ========== PRUEBA 5: MOSTRAR EN DIFERENTES MODOS ==========
print("\n✅ PRUEBA 5: Mostrar información en diferentes modos")
print(cliente1.mostrar_informacion("basico"))
print(cliente1.mostrar_informacion("normal"))

print("\n" + "=" * 60)
print("FIN DE LAS PRUEBAS")
print("=" * 60)