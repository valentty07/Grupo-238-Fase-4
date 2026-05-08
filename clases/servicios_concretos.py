"""
MÓDULO DE SERVICIOS CONCRETOS
Sistema de Gestión Software FJ - Fase 4
"""

from .servicio import Servicio
from .excepciones import ParametrosInvalidosException

class AlquilerEquipos(Servicio):
    """Alquiler de equipos tecnológicos"""
    
    def __init__(self, nombre, descripcion, precio_base, tipo_equipo, disponible=True, id_servicio=None):
        super().__init__(nombre, descripcion, precio_base, disponible, id_servicio)
        self._tipo_equipo = tipo_equipo
    
    def calcular_costo(self, dias, seguro=False, **kwargs):
        if dias <= 0:
            raise ParametrosInvalidosException("dias", "Los días deben ser mayores a cero")
        costo = self._precio_base * dias
        if seguro:
            costo += costo * 0.10
        return costo
    
    def describir_servicio(self):
        return f"Alquiler de equipo: {self._tipo_equipo}"


class Asesoria(Servicio):
    """Asesorías especializadas"""
    
    def __init__(self, nombre, descripcion, precio_base, especialidad, disponible=True, id_servicio=None):
        super().__init__(nombre, descripcion, precio_base, disponible, id_servicio)
        self._especialidad = especialidad
    
    def calcular_costo(self, horas, material_apoyo=False, **kwargs):
        if horas <= 0:
            raise ParametrosInvalidosException("horas", "Las horas deben ser mayores a cero")
        costo = self._precio_base * horas
        if material_apoyo:
            costo += costo * 0.15
        return costo
    
    def describir_servicio(self):
        return f"Asesoría especializada en: {self._especialidad}"