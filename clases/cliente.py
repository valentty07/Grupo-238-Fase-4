"""
MÓDULO DE CLASE CLIENTE
Estudiante 1 - Sistema de Gestión Software FJ
Fase 4 - Encapsulación y validaciones
"""

import re
from .entidad import Entidad
from .excepciones import DatosClienteInvalidosException

class Cliente(Entidad):
    """Clase que representa un cliente con validaciones robustas"""
    
    def __init__(self, nombre, email, telefono, identificacion, id_cliente=None):
        super().__init__(id_cliente)
        
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.identificacion = identificacion
        
        self._reservas_activas = []
        self._historial_reservas = []
        
        self.actualizar_timestamp()
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        if not valor or not isinstance(valor, str):
            raise DatosClienteInvalidosException("nombre", "El nombre no puede estar vacío")
        
        valor = valor.strip()
        if len(valor) < 3:
            raise DatosClienteInvalidosException("nombre", "El nombre debe tener al menos 3 caracteres")
        
        self._nombre = valor
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, valor):
        if not valor or not isinstance(valor, str):
            raise DatosClienteInvalidosException("email", "El email no puede estar vacío")
        
        valor = valor.strip().lower()
        
        patron_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(patron_email, valor):
            raise DatosClienteInvalidosException("email", f"Formato de email inválido: {valor}")
        
        self._email = valor
    
    @property
    def telefono(self):
        return self._telefono
    
    @telefono.setter
    def telefono(self, valor):
        if not valor or not isinstance(valor, str):
            raise DatosClienteInvalidosException("telefono", "El teléfono no puede estar vacío")
        
        valor = valor.strip()
        digitos = re.sub(r'[^\d]', '', valor)
        
        if len(digitos) < 7:
            raise DatosClienteInvalidosException("telefono", "El teléfono debe tener al menos 7 dígitos")
        
        self._telefono = valor
    
    @property
    def identificacion(self):
        return self._identificacion
    
    @identificacion.setter
    def identificacion(self, valor):
        if not valor or not isinstance(valor, str):
            raise DatosClienteInvalidosException("identificacion", "La identificación no puede estar vacía")
        
        valor = valor.strip()
        if len(valor) < 5:
            raise DatosClienteInvalidosException("identificacion", "La identificación debe tener al menos 5 caracteres")
        
        self._identificacion = valor
    
    @property
    def reservas_activas(self):
        return self._reservas_activas.copy()
    
    @property
    def historial_reservas(self):
        return self._historial_reservas.copy()
    
    def agregar_reserva(self, reserva):
        self._reservas_activas.append(reserva)
        self.actualizar_timestamp()
    
    def mover_reserva_a_historial(self, reserva):
        if reserva in self._reservas_activas:
            self._reservas_activas.remove(reserva)
            self._historial_reservas.append(reserva)
            self.actualizar_timestamp()
    
    def obtener_total_gastado(self):
        total = 0
        for reserva in self._historial_reservas:
            total += reserva.costo_total
        for reserva in self._reservas_activas:
            total += reserva.costo_total
        return total
    
    def validar_datos(self):
        try:
            self.nombre = self._nombre
            self.email = self._email
            self.telefono = self._telefono
            self.identificacion = self._identificacion
            return True
        except DatosClienteInvalidosException as e:
            raise DatosClienteInvalidosException(e.campo, f"Validación fallida: {e.razon}")
    
    def mostrar_informacion(self, modo="completo"):
        if modo == "basico":
            return f"Cliente: {self.nombre} | ID: {self.id}"
        
        elif modo == "normal":
            return (f"--- CLIENTE ---\n"
                    f"ID: {self.id}\n"
                    f"Nombre: {self.nombre}\n"
                    f"Email: {self.email}\n"
                    f"Teléfono: {self.telefono}")
        
        elif modo == "completo":
            return (f"=== CLIENTE (DETALLE COMPLETO) ===\n"
                    f"ID: {self.id}\n"
                    f"Nombre: {self.nombre}\n"
                    f"Email: {self.email}\n"
                    f"Teléfono: {self.telefono}\n"
                    f"Identificación: {self.identificacion}")
        
        else:
            return f"Modo no válido: {modo}"
    
    def __str__(self):
        return self.mostrar_informacion("normal")