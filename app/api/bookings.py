from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.schemas.booking_schema import ReservaCreate, ReservaResponse
from app.services.create_booking_service import CrearReservaService
from app.services.obtener_reservas_service import ObtenerReservasService
from app.repositories.mongo_booking_repository import MongoReservaRepository
from app.core.database import get_database

router = APIRouter(prefix="/bookings", tags=["Reservas"])

def obtener_servicio_crear_reserva(db: AsyncIOMotorDatabase = Depends(get_database)) -> CrearReservaService:
    repositorio = MongoReservaRepository(db)
    return CrearReservaService(repositorio)

def obtener_servicio_obtener_reservas(db: AsyncIOMotorDatabase = Depends(get_database)) -> ObtenerReservasService:
    repositorio = MongoReservaRepository(db)
    return ObtenerReservasService(repositorio)

@router.post("", response_model=ReservaResponse, status_code=status.HTTP_201_CREATED)
async def crear_reserva(
    reserva_in: ReservaCreate,
    servicio: CrearReservaService = Depends(obtener_servicio_crear_reserva)
):
    try:
        reserva = await servicio.ejecutar(
            datos_padre=reserva_in.padre.model_dump(),
            datos_servicio=reserva_in.detalles_servicio.model_dump(),
            datos_ninos=[nino.model_dump() for nino in reserva_in.ninos]
        )
        
        return ReservaResponse(
            id=reserva.id,
            padre=reserva.padre.__dict__,
            detalles_servicio=reserva.detalles_servicio.__dict__,
            ninos=[nino.__dict__ for nino in reserva.ninos],
            creado_en=reserva.creado_en
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("", response_model=List[ReservaResponse], status_code=status.HTTP_200_OK)
async def obtener_reservas(
    servicio: ObtenerReservasService = Depends(obtener_servicio_obtener_reservas)
):
    try:
        reservas = await servicio.ejecutar()
        
        return [
            ReservaResponse(
                id=r.id,
                padre=r.padre.__dict__,
                detalles_servicio=r.detalles_servicio.__dict__,
                ninos=[n.__dict__ for n in r.ninos],
                creado_en=r.creado_en
            ) for r in reservas
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
