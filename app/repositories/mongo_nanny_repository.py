from typing import List, Optional
from uuid import UUID
from datetime import datetime
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.repositories.nanny_repository import NineraRepository
from app.models.nanny import Ninera, Resena

class MongoNineraRepository(NineraRepository):
    def __init__(self, db: AsyncIOMotorDatabase):
        self.coleccion = db.nannies

    async def guardar(self, ninera: Ninera) -> None:
        documento = {
            "_id": str(ninera.id),
            "nombre_completo": ninera.nombre_completo,
            "foto_url": str(ninera.foto_url),
            "titulo": ninera.titulo,
            "descripcion": ninera.descripcion,
            "resenas": [],  # Inicialmente vacío
            "creado_en": ninera.creado_en.isoformat()
        }
        await self.coleccion.insert_one(documento)

    async def obtener_todas(self) -> List[Ninera]:
        cursor = self.coleccion.find()
        nineras = []
        async for doc in cursor:
            nineras.append(self._mapear_documento_a_entidad(doc))
        return nineras

    async def obtener_por_id(self, id: UUID) -> Optional[Ninera]:
        doc = await self.coleccion.find_one({"_id": str(id)})
        if not doc:
            return None
        return self._mapear_documento_a_entidad(doc)

    async def agregar_resena(self, ninera_id: UUID, resena: Resena) -> bool:
        doc_resena = {
            "numero_contrato": resena.numero_contrato,
            "calificacion": resena.calificacion,
            "comentario": resena.comentario,
            "fecha": resena.fecha.isoformat()
        }
        resultado = await self.coleccion.update_one(
            {"_id": str(ninera_id)},
            {"$push": {"resenas": doc_resena}}
        )
        return resultado.modified_count > 0

    def _mapear_documento_a_entidad(self, doc: dict) -> Ninera:
        resenas_vo = [
            Resena(
                numero_contrato=r["numero_contrato"],
                calificacion=r["calificacion"],
                comentario=r["comentario"],
                fecha=datetime.fromisoformat(r["fecha"])
            ) for r in doc.get("resenas", [])
        ]
        
        return Ninera(
            id=UUID(doc["_id"]),
            nombre_completo=doc["nombre_completo"],
            foto_url=doc["foto_url"],
            titulo=doc["titulo"],
            descripcion=doc["descripcion"],
            resenas=resenas_vo,
            creado_en=datetime.fromisoformat(doc["creado_en"])
        )
