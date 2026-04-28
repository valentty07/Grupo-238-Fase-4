"""
MÓDULO DE CLASE ABSTRACTA ENTIDAD
Estudiante 1 - Sistema de Gestión Software FJ
Fase 4 - Abstracción y herencia
"""

from abc import ABC, abstractmethod
from datetime import datetime

class Entidad(ABC):
    """Clase abstracta base para todas las entidades del sistema"""
    
    _contador_ids = {}
    
    def __init__(self, id_entidad=None):
        if id_entidad:
            self._id = id_entidad
        else:
            self._id = self._generar_id()
        
        self._fecha_creacion = datetime.now()
        self._fecha_actualizacion = datetime.now()
    
    @property
    def id(self):
        return self._id
    
    @property
    def fecha_creacion(self):
        return self._fecha_creacion
    
    @property
    def fecha_actualizacion(self):
        return self._fecha_actualizacion
    
    def _generar_id(self):
        nombre_clase = self.__class__.__name__
        
        if nombre_clase not in Entidad._contador_ids:
            Entidad._contador_ids[nombre_clase] = 1
        else:
            Entidad._contador_ids[nombre_clase] += 1
        
        numero = Entidad._contador_ids[nombre_clase]
        return f"{nombre_clase}_{numero:03d}"
    
    @abstractmethod
    def mostrar_informacion(self):
        pass
    
    @abstractmethod
    def validar_datos(self):
        pass
    
    def actualizar_timestamp(self):
        self._fecha_actualizacion = datetime.now()
    
    def __str__(self):
        return f"{self.__class__.__name__}[id={self._id}]"