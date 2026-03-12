from typing import List, Optional
from uuid import UUID
from app.repositories.nanny_repository import NineraRepository
from app.models.nanny import Ninera

class GetNinerasService:
    def __init__(self, repositorio: NineraRepository):
        self.repositorio = repositorio
        
    async def obtener_todas(self) -> List[Ninera]:
        """Obtiene la lista completa de niñeras."""
        return await self.repositorio.obtener_todas()
        
    async def obtener_por_id(self, ninera_id: UUID) -> Optional[Ninera]:
        """Obtiene el detalle de una niñera por su ID incluyendo sus reseñas."""
        return await self.repositorio.obtener_por_id(ninera_id)
