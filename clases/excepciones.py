"""
MÓDULO DE EXCEPCIONES PERSONALIZADAS
Sistema de Gestión Software FJ - Fase 4
"""

class SoftwareFJException(Exception):
    """Excepción base para todo el sistema"""
    def __init__(self, mensaje="Error en el sistema Software FJ"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class ClienteException(SoftwareFJException):
    """Excepción base para errores de clientes"""
    pass


class ClienteNoEncontradoException(ClienteException):
    """Se lanza cuando no se encuentra un cliente"""
    def __init__(self, identificador):
        self.identificador = identificador
        super().__init__(f"Cliente no encontrado: {identificador}")


class ClienteYaExisteException(ClienteException):
    """Se lanza cuando ya existe un cliente"""
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


class ParametrosInvalidosException(SoftwareFJException):
    """Se lanza cuando hay parámetros inválidos"""
    def __init__(self, parametro, razon):
        self.parametro = parametro
        self.razon = razon
        super().__init__(f"Parámetro inválido '{parametro}': {razon}")


class ReservaException(SoftwareFJException):
    """Excepción base para errores de reservas"""
    pass


class ReservaInvalidaException(ReservaException):
    """Se lanza cuando una reserva no es válida"""
    def __init__(self, razon):
        self.razon = razon
        super().__init__(f"Reserva inválida: {razon}")


class CancelacionNoPermitidaException(ReservaException):
    """Se lanza cuando no se puede cancelar una reserva"""
    def __init__(self, estado_actual):
        self.estado_actual = estado_actual
        super().__init__(f"No se puede cancelar la reserva. Estado actual: {estado_actual}")