"""
MÓDULO DE SERVICIOS - COMPLETADO
Sistema de Gestión Software FJ - Fase 4
"""

from abc import ABC, abstractmethod
from .entidad import Entidad
from .excepciones import ParametrosInvalidosException

class Servicio(Entidad, ABC):
    """Clase abstracta para los servicios de Software FJ"""
    
    def __init__(self, nombre, descripcion, precio_base, disponible=True, id_servicio=None):
        super().__init__(id_servicio)
        self._nombre = nombre
        self._descripcion = descripcion
        self._precio_base = precio_base
        self._disponible = disponible
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def precio_base(self):
        return self._precio_base
    
    @property
    def disponible(self):
        return self._disponible
    
    def validar_datos(self):
        if self._precio_base <= 0:
            raise ParametrosInvalidosException("precio_base", "El precio base debe ser mayor a cero")
        return True
    
    @abstractmethod
    def calcular_costo(self, **kwargs):
        pass
    
    @abstractmethod
    def describir_servicio(self):
        pass
    
    def mostrar_informacion(self):
        return f"Servicio: {self._nombre} | Precio base: ${self._precio_base:.2f} | Disponible: {self._disponible}"


class ReservaSalas(Servicio):
    """Clase para reserva de salas de reuniones"""
    
    def __init__(self, nombre, descripcion, precio_base, capacidad, equipamiento=None, disponible=True, id_servicio=None):
        super().__init__(nombre, descripcion, precio_base, disponible, id_servicio)
        self._capacidad = capacidad
        self._equipamiento = equipamiento if equipamiento else []
    
    def calcular_costo(self, horas, con_equipamiento_extra=False, **kwargs):
        if horas <= 0:
            raise ParametrosInvalidosException("horas", "Las horas deben ser mayores a cero")
        costo = self._precio_base * horas
        if con_equipamiento_extra:
            costo += costo * 0.20  # 20% extra por equipamiento
        return costo
    
    def describir_servicio(self):
        equipos = ", ".join(self._equipamiento) if self._equipamiento else "Ninguno"
        return f"Reserva de sala con capacidad para {self._capacidad} personas. Equipamiento: {equipos}"