from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID
from app.models.nanny import Ninera, Resena

class NineraRepository(ABC):
    @abstractmethod
    async def guardar(self, ninera: Ninera) -> None:
        pass

    @abstractmethod
    async def obtener_todas(self) -> List[Ninera]:
        pass

    @abstractmethod
    async def obtener_por_id(self, id: UUID) -> Optional[Ninera]:
        pass

    @abstractmethod
    async def agregar_resena(self, ninera_id: UUID, resena: Resena) -> bool:
        """Añade una nueva reseña al perfil de la niñera en la BD. Retorna True si fue exitoso."""
        pass
