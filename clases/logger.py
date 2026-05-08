"""
MÓDULO DE GESTOR DE LOGS
Sistema de Gestión Software FJ - Fase 4
"""

import logging
import os

class GestorLogs:
    """Clase para gestionar el registro de eventos y errores"""
    
    def __init__(self, archivo_log="logs/sistema.log"):
        os.makedirs("logs", exist_ok=True)
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(archivo_log, encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def registrar_evento(self, mensaje, nivel="INFO"):
        if nivel == "INFO":
            self.logger.info(mensaje)
        elif nivel == "WARNING":
            self.logger.warning(mensaje)
        elif nivel == "ERROR":
            self.logger.error(mensaje)
        elif nivel == "DEBUG":
            self.logger.debug(mensaje)
    
    def registrar_error(self, error, contexto=""):
        mensaje = f"Error: {error}"
        if contexto:
            mensaje = f"{contexto} - {mensaje}"
        self.logger.error(mensaje)
    
    def registrar_operacion(self, operacion, resultado, detalles=""):
        mensaje = f"Operación: {operacion} | Resultado: {resultado}"
        if detalles:
            mensaje = f"{mensaje} | Detalles: {detalles}"
        self.logger.info(mensaje)