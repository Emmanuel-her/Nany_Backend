from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.schemas.nanny_schema import NineraCreate, NineraResponse, ResenaCreate
from app.services.create_nanny_service import CreateNineraService
from app.services.get_nannies_service import GetNinerasService
from app.services.add_review_service import AddReviewService
from app.repositories.mongo_nanny_repository import MongoNineraRepository
from app.core.database import get_database

router = APIRouter(prefix="/nannies", tags=["Niñeras"])

def obtener_servicio_crear(db: AsyncIOMotorDatabase = Depends(get_database)) -> CreateNineraService:
    repositorio = MongoNineraRepository(db)
    return CreateNineraService(repositorio)

def obtener_servicio_get(db: AsyncIOMotorDatabase = Depends(get_database)) -> GetNinerasService:
    repositorio = MongoNineraRepository(db)
    return GetNinerasService(repositorio)

def obtener_servicio_review(db: AsyncIOMotorDatabase = Depends(get_database)) -> AddReviewService:
    repositorio = MongoNineraRepository(db)
    return AddReviewService(repositorio)

@router.post("", response_model=NineraResponse, status_code=status.HTTP_201_CREATED)
async def registrar_ninera(
    ninera_in: NineraCreate,
    servicio: CreateNineraService = Depends(obtener_servicio_crear)
):
    try:
        ninera = await servicio.ejecutar(ninera_in.model_dump(mode='json'))
        
        return NineraResponse(
            id=ninera.id,
            nombre_completo=ninera.nombre_completo,
            foto_url=ninera.foto_url,
            titulo=ninera.titulo,
            descripcion=ninera.descripcion,
            resenas=[],
            creado_en=ninera.creado_en
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("", response_model=List[NineraResponse], status_code=status.HTTP_200_OK)
async def listar_nineras(
    servicio: GetNinerasService = Depends(obtener_servicio_get)
):
    try:
        nineras = await servicio.obtener_todas()
        
        return [
            NineraResponse(
                id=n.id,
                nombre_completo=n.nombre_completo,
                foto_url=n.foto_url,
                titulo=n.titulo,
                descripcion=n.descripcion,
                resenas=[r.__dict__ for r in n.resenas],
                creado_en=n.creado_en
            ) for n in nineras
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{id}", response_model=NineraResponse, status_code=status.HTTP_200_OK)
async def obtener_perfil_ninera(
    id: UUID,
    servicio: GetNinerasService = Depends(obtener_servicio_get)
):
    try:
        ninera = await servicio.obtener_por_id(id)
        if not ninera:
            raise HTTPException(status_code=404, detail="Niñera no encontrada")
            
        return NineraResponse(
            id=ninera.id,
            nombre_completo=ninera.nombre_completo,
            foto_url=ninera.foto_url,
            titulo=ninera.titulo,
            descripcion=ninera.descripcion,
            resenas=[r.__dict__ for r in ninera.resenas],
            creado_en=ninera.creado_en
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/{id}/reviews", status_code=status.HTTP_201_CREATED)
async def agregar_resena(
    id: UUID,
    resena_in: ResenaCreate,
    servicio: AddReviewService = Depends(obtener_servicio_review)
):
    try:
        exito = await servicio.ejecutar(id, resena_in.model_dump())
        if not exito:
            raise HTTPException(status_code=404, detail="Niñera no encontrada o fallo al insertar la reseña")
            
        return {"mensaje": "Reseña guardada exitosamente"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
