from uuid import UUID
from typing import Optional
from app.repositories.nanny_repository import NineraRepository
from app.models.nanny import Resena

class AddReviewService:
    def __init__(self, repositorio: NineraRepository):
        self.repositorio = repositorio
        
    async def ejecutar(self, ninera_id: UUID, datos_resena: dict) -> bool:
        # 1. Validar que la niñera exista primero
        ninera = await self.repositorio.obtener_por_id(ninera_id)
        if not ninera:
            return False
            
        # 2. Reconstruir el Value Object de la reseña utilizando los datos del Request Schema
        resena = Resena(**datos_resena)
        
        # 3. Guardarla en base de datos al perfil de la niñera
        return await self.repositorio.agregar_resena(ninera_id, resena)
