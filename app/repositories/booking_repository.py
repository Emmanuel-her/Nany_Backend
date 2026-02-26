from abc import ABC, abstractmethod
from typing import List
from app.models.booking import Reserva

class ReservaRepository(ABC):
    @abstractmethod
    async def guardar(self, reserva: Reserva) -> None:
        """Guarda la entidad reserva en la capa de persistencia"""
        pass

    @abstractmethod
    async def obtener_todas(self) -> List[Reserva]:
        """Obtiene todas las reservas desde la capa de persistencia"""
        pass
