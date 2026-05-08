"""
MÓDULO DE RESERVA
Sistema de Gestión Software FJ - Fase 4
"""

from datetime import datetime
from .entidad import Entidad
from .excepciones import ReservaInvalidaException, CancelacionNoPermitidaException

class Reserva(Entidad):
    """Clase que gestiona las reservas"""
    
    ESTADOS = ["PENDIENTE", "CONFIRMADA", "CANCELADA", "COMPLETADA"]
    
    def __init__(self, cliente, servicio, fecha_reserva, duracion, id_reserva=None):
        super().__init__(id_reserva)
        self._cliente = cliente
        self._servicio = servicio
        self._fecha_reserva = fecha_reserva
        self._duracion = duracion
        self._estado = "PENDIENTE"
        self._costo_total = self.calcular_costo_total()
        cliente.agregar_reserva(self)
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def servicio(self):
        return self._servicio
    
    @property
    def estado(self):
        return self._estado
    
    @property
    def costo_total(self):
        return self._costo_total
    
    def calcular_costo_total(self, descuento=0, impuesto=0):
        costo_base = self._servicio.calcular_costo(horas=self._duracion)
        
        if descuento > 0:
            costo_base = costo_base * (1 - descuento / 100)
        
        if impuesto > 0:
            costo_base = costo_base * (1 + impuesto / 100)
        
        return costo_base
    
    def confirmar(self):
        if self._estado != "PENDIENTE":
            raise CancelacionNoPermitidaException(self._estado)
        self._estado = "CONFIRMADA"
        self.actualizar_timestamp()
    
    def cancelar(self):
        if self._estado not in ["PENDIENTE", "CONFIRMADA"]:
            raise CancelacionNoPermitidaException(self._estado)
        self._estado = "CANCELADA"
        self.actualizar_timestamp()
        self._cliente.mover_reserva_a_historial(self)
    
    def completar(self):
        if self._estado != "CONFIRMADA":
            raise CancelacionNoPermitidaException(self._estado)
        self._estado = "COMPLETADA"
        self.actualizar_timestamp()
        self._cliente.mover_reserva_a_historial(self)
    
    def validar_datos(self):
        if not self._cliente:
            raise ReservaInvalidaException("Cliente no válido")
        if not self._servicio:
            raise ReservaInvalidaException("Servicio no válido")
        if self._duracion <= 0:
            raise ReservaInvalidaException("La duración debe ser mayor a cero")
        return True
    
    def mostrar_informacion(self, modo="normal"):
        if modo == "basico":
            return f"Reserva: {self.id} | Estado: {self._estado}"
        else:
            return (f"=== RESERVA ===\n"
                    f"ID: {self.id}\n"
                    f"Cliente: {self._cliente.nombre}\n"
                    f"Servicio: {self._servicio.nombre}\n"
                    f"Duración: {self._duracion} horas\n"
                    f"Costo total: ${self._costo_total:.2f}\n"
                    f"Estado: {self._estado}")