from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import Optional

class EstadoEstudio(Enum):
    INICIADO = auto()
    PRESUPUESTADO = auto()
    PAGADO = auto()
    AUTORIZADO = auto()
    TURNO_CONFIRMADO = auto()
    REALIZADA = auto()
    CENTRALIZADA = auto()
    ENVIADA_AL_EXTERIOR = auto()
    FINALIZADO = auto()
    CANCELADO = auto()

class EstadoBase(ABC):
    @abstractmethod
    def siguiente_estado(self, estudio: 'Estudio') -> bool:
        pass
    
    def cancelar(self, estudio: 'Estudio') -> bool:
        estudio.estado_actual = EstadoCancelado()
        return True

class EstadoIniciado(EstadoBase):
    def siguiente_estado(self, estudio: 'Estudio') -> bool:
        estudio.estado_actual = EstadoPresupuestado()
        return True

class EstadoPresupuestado(EstadoBase):
    def siguiente_estado(self, estudio: 'Estudio') -> bool:
        estudio.estado_actual = EstadoPagado()
        return True

class EstadoPagado(EstadoBase):
    def siguiente_estado(self, estudio: 'Estudio') -> bool:
        estudio.estado_actual = EstadoAutorizado()
        return True

class EstadoAutorizado(EstadoBase):
    def siguiente_estado(self, estudio: 'Estudio') -> bool:
        estudio.estado_actual = EstadoTurnoConfirmado()
        return True

class EstadoTurnoConfirmado(EstadoBase):
    def siguiente_estado(self, estudio: 'Estudio') -> bool:
        estudio.estado_actual = EstadoRealizada()
        return True

class EstadoRealizada(EstadoBase):
    def siguiente_estado(self, estudio: 'Estudio') -> bool:
        estudio.estado_actual = EstadoCentralizada()
        return True

class EstadoCentralizada(EstadoBase):
    def siguiente_estado(self, estudio: 'Estudio') -> bool:
        estudio.estado_actual = EstadoEnviadaAlExterior()
        return True

class EstadoEnviadaAlExterior(EstadoBase):
    def siguiente_estado(self, estudio: 'Estudio') -> bool:
        estudio.estado_actual = EstadoFinalizado()
        return True

class EstadoFinalizado(EstadoBase):
    def siguiente_estado(self, estudio: 'Estudio') -> bool:
        return False  # No hay siguiente estado después de finalizado

class EstadoCancelado(EstadoBase):
    def siguiente_estado(self, estudio: 'Estudio') -> bool:
        return False  # No hay siguiente estado después de cancelado
    
    def cancelar(self, estudio: 'Estudio') -> bool:
        return False  # No se puede cancelar un estudio ya cancelado