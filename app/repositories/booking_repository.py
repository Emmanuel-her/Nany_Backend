from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID
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

    @abstractmethod
    async def obtener_por_id(self, id: UUID) -> Optional[Reserva]:
        """Obtiene una reserva específica por su ID"""
        pass
