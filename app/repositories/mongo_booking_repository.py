from typing import List
from uuid import UUID
from datetime import datetime, date, time
from app.repositories.booking_repository import ReservaRepository
from app.models.booking import Reserva, Padre, DetallesServicio, Nino, TipoServicio
from motor.motor_asyncio import AsyncIOMotorDatabase

class MongoReservaRepository(ReservaRepository):
    def __init__(self, db: AsyncIOMotorDatabase):
        self.coleccion = db.bookings

    async def guardar(self, reserva: Reserva) -> None:
        documento = {
            "_id": str(reserva.id),
            "padre": {
                "nombre_completo": reserva.padre.nombre_completo,
                "numero_documento": reserva.padre.numero_documento,
                "telefono_whatsapp": reserva.padre.telefono_whatsapp
            },
            "detalles_servicio": {
                "fecha_inicio": reserva.detalles_servicio.fecha_inicio.isoformat(),
                "hora_inicio": reserva.detalles_servicio.hora_inicio.isoformat(),
                "tipo": reserva.detalles_servicio.tipo.value,
                "estado": reserva.detalles_servicio.estado
            },
            "ninos": [
                {
                    "edad": nino.edad,
                    "condiciones_especiales": nino.condiciones_especiales
                } for nino in reserva.ninos
            ],
            "creado_en": reserva.creado_en.isoformat()
        }
        await self.coleccion.insert_one(documento)

    async def obtener_todas(self) -> List[Reserva]:
        cursor = self.coleccion.find()
        reservas = []
        async for doc in cursor:
            # Reconstruir Value Objects
            padre = Padre(
                nombre_completo=doc["padre"]["nombre_completo"],
                numero_documento=doc["padre"]["numero_documento"],
                telefono_whatsapp=doc["padre"]["telefono_whatsapp"]
            )
            detalles_servicio = DetallesServicio(
                fecha_inicio=date.fromisoformat(doc["detalles_servicio"]["fecha_inicio"]),
                hora_inicio=time.fromisoformat(doc["detalles_servicio"]["hora_inicio"]),
                tipo=TipoServicio(doc["detalles_servicio"]["tipo"]),
                estado=doc["detalles_servicio"]["estado"]
            )
            ninos = [
                Nino(
                    edad=n["edad"],
                    condiciones_especiales=n["condiciones_especiales"]
                ) for n in doc["ninos"]
            ]
            
            # Reconstruir Entity
            reserva = Reserva(
                padre=padre,
                detalles_servicio=detalles_servicio,
                ninos=ninos,
                id=UUID(doc["_id"]),
                creado_en=datetime.fromisoformat(doc["creado_en"])
            )
            reservas.append(reserva)
        return reservas
