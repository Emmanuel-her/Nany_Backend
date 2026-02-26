from typing import List
from app.repositories.booking_repository import ReservaRepository
from app.models.booking import Reserva

class ObtenerReservasService:
    def __init__(self, repositorio: ReservaRepository):
        self.repositorio = repositorio

    async def ejecutar(self) -> List[Reserva]:
        # Obtiene todas las reservas de la base de datos a través del Puerto
        return await self.repositorio.obtener_todas()
