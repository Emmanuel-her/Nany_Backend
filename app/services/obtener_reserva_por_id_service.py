from uuid import UUID
from typing import Optional
from app.repositories.booking_repository import ReservaRepository
from app.models.booking import Reserva

class ObtenerReservaPorIdService:
    def __init__(self, repositorio: ReservaRepository):
        self.repositorio = repositorio

    async def ejecutar(self, id: UUID) -> Optional[Reserva]:
        # Obtiene una reserva específica de la base de datos a través del Puerto
        return await self.repositorio.obtener_por_id(id)
