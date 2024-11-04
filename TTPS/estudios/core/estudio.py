# class Estudio:
#     def __init__(self):
#         self.estado_actual: EstadoBase = EstadoIniciado()
#         self._historial_estados = [EstadoEstudio.INICIADO]

#     @property
#     def estado(self) -> EstadoEstudio:
#         # Mapeo de clases de estado a enum EstadoEstudio
#         estado_a_enum = {
#             EstadoIniciado: EstadoEstudio.INICIADO,
#             EstadoPresupuestado: EstadoEstudio.PRESUPUESTADO,
#             EstadoPagado: EstadoEstudio.PAGADO,
#             EstadoAutorizado: EstadoEstudio.AUTORIZADO,
#             EstadoTurnoConfirmado: EstadoEstudio.TURNO_CONFIRMADO,
#             EstadoRealizada: EstadoEstudio.REALIZADA,
#             EstadoCentralizada: EstadoEstudio.CENTRALIZADA,
#             EstadoEnviadaAlExterior: EstadoEstudio.ENVIADA_AL_EXTERIOR,
#             EstadoFinalizado: EstadoEstudio.FINALIZADO,
#             EstadoCancelado: EstadoEstudio.CANCELADO
#         }
#         return estado_a_enum[type(self.estado_actual)]

#     def avanzar_estado(self) -> bool:
#         """Intenta avanzar al siguiente estado en la secuencia."""
#         resultado = self.estado_actual.siguiente_estado(self)
#         if resultado:
#             self._historial_estados.append(self.estado)
#         return resultado

#     def cancelar(self) -> bool:
#         """Intenta cancelar el estudio."""
#         resultado = self.estado_actual.cancelar(self)
#         if resultado:
#             self._historial_estados.append(EstadoEstudio.CANCELADO)
#         return resultado

#     @property
#     def historial_estados(self) -> list[EstadoEstudio]:
#         """Retorna el historial de estados por los que pasó el estudio."""
#         return self._historial_estados.copy()