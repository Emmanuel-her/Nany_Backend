from app.repositories.booking_repository import ReservaRepository
from app.services.notification_service import NotificationService
from app.models.booking import Reserva, Padre, Nino, DetallesServicio

class CrearReservaService:
    def __init__(self, repositorio: ReservaRepository, notification_service: NotificationService = None):
        self.repositorio = repositorio
        self.notification_service = notification_service

    async def ejecutar(self, numero_contrato: str, datos_padre: dict, datos_servicio: dict, datos_ninos: list) -> Reserva:
        # Crear Value Objects
        padre = Padre(**datos_padre)
        detalles_servicio = DetallesServicio(**datos_servicio)
        ninos = [Nino(**nino) for nino in datos_ninos]
        
        # Crear Entidad principal
        reserva = Reserva(
            numero_contrato=numero_contrato,
            padre=padre,
            detalles_servicio=detalles_servicio,
            ninos=ninos
        )
        
        # Persistir a través del Puerto del Repositorio
        await self.repositorio.guardar(reserva)
        
        # Enviar notificación push
        if self.notification_service:
            self.notification_service.enviar_notificacion(
                titulo="Nueva Reserva",
                cuerpo="Se ha realizado una solicitud de reserva"
            )
        
        return reserva
