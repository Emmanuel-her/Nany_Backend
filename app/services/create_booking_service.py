from app.repositories.booking_repository import ReservaRepository
from app.models.booking import Reserva, Padre, Nino, DetallesServicio

class CrearReservaService:
    def __init__(self, repositorio: ReservaRepository):
        self.repositorio = repositorio

    async def ejecutar(self, datos_padre: dict, datos_servicio: dict, datos_ninos: list) -> Reserva:
        # Crear Value Objects
        padre = Padre(**datos_padre)
        detalles_servicio = DetallesServicio(**datos_servicio)
        ninos = [Nino(**nino) for nino in datos_ninos]
        
        # Crear Entidad principal
        reserva = Reserva(
            padre=padre,
            detalles_servicio=detalles_servicio,
            ninos=ninos
        )
        
        # Persistir a través del Puerto del Repositorio
        await self.repositorio.guardar(reserva)
        
        return reserva
