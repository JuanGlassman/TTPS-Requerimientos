from abc import ABC, abstractmethod
from models import EstadoEstudio

class EstadoBase(ABC):
    @abstractmethod
    def siguiente_estado(self, estudio) -> bool:
        pass
    
    def cancelar(self, estudio) -> bool:
        estudio.estado = EstadoEstudio.CANCELADO
        estudio.save()
        return True

class EstadoIniciado(EstadoBase):
    def siguiente_estado(self, estudio) -> bool:
        estudio.estado = EstadoEstudio.PRESUPUESTADO
        estudio.save()
        return True

class EstadoPresupuestado(EstadoBase):
    def siguiente_estado(self, estudio) -> bool:
        estudio.estado = EstadoEstudio.PAGADO
        estudio.save()
        return True

class EstadoPagado(EstadoBase):
    def siguiente_estado(self, estudio) -> bool:
        estudio.estado = EstadoEstudio.AUTORIZADO
        estudio.save()
        return True

class EstadoAutorizado(EstadoBase):
    def siguiente_estado(self, estudio) -> bool:
        estudio.estado = EstadoEstudio.TURNO_CONFIRMADO
        estudio.save()
        return True

class EstadoTurnoConfirmado(EstadoBase):
    def siguiente_estado(self, estudio) -> bool:
        estudio.estado = EstadoEstudio.REALIZADA
        estudio.save()
        return True

class EstadoRealizada(EstadoBase):
    def siguiente_estado(self, estudio) -> bool:
        estudio.estado = EstadoEstudio.CENTRALIZADA
        estudio.save()
        return True

class EstadoCentralizada(EstadoBase):
    def siguiente_estado(self, estudio) -> bool:
        estudio.estado = EstadoEstudio.ENVIADA_EXTERIOR
        estudio.save()
        return True

class EstadoEnviadaExterior(EstadoBase):
    def siguiente_estado(self, estudio) -> bool:
        estudio.estado = EstadoEstudio.FINALIZADO
        estudio.save()
        return True

class EstadoFinalizado(EstadoBase):
    def siguiente_estado(self, estudio) -> bool:
        return False

class EstadoCancelado(EstadoBase):
    def siguiente_estado(self, estudio) -> bool:
        return False
    
    def cancelar(self, estudio) -> bool:
        return False