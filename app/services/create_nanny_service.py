from app.repositories.nanny_repository import NineraRepository
from app.models.nanny import Ninera

class CreateNineraService:
    def __init__(self, repositorio: NineraRepository):
        self.repositorio = repositorio
        
    async def ejecutar(self, datos_ninera: dict) -> Ninera:
        # Crear la entidad de dominio Ninera en base al diccionario del schema de entrada
        ninera = Ninera(**datos_ninera)
        
        # Guardar en persistencia
        await self.repositorio.guardar(ninera)
        
        return ninera
