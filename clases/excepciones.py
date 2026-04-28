"""
MÓDULO DE EXCEPCIONES PERSONALIZADAS
Estudiante 1 - Sistema de Gestión Software FJ
Fase 4 - Manejo de excepciones
"""

class SoftwareFJException(Exception):
    """Excepción base para todo el sistema"""
    def __init__(self, mensaje="Error en el sistema Software FJ"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class ClienteException(SoftwareFJException):
    """Excepción base para errores relacionados con clientes"""
    pass


class ClienteNoEncontradoException(ClienteException):
    """Se lanza cuando no se encuentra un cliente"""
    def __init__(self, identificador):
        self.identificador = identificador
        super().__init__(f"Cliente no encontrado: {identificador}")


class ClienteYaExisteException(ClienteException):
    """Se lanza cuando ya existe un cliente con mismo ID o email"""
    def __init__(self, campo, valor):
        self.campo = campo
        self.valor = valor
        super().__init__(f"Ya existe un cliente con {campo}: {valor}")


class DatosClienteInvalidosException(ClienteException):
    """Se lanza cuando los datos del cliente no son válidos"""
    def __init__(self, campo, razon):
        self.campo = campo
        self.razon = razon
        super().__init__(f"Dato inválido en '{campo}': {razon}")