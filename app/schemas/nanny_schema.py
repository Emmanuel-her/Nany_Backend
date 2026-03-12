from pydantic import BaseModel, Field, HttpUrl
from typing import List
from datetime import datetime
from uuid import UUID

class ResenaCreate(BaseModel):
    numero_contrato: str = Field(..., min_length=1, description="Número de contrato o reserva para validar la procedencia")
    calificacion: int = Field(..., ge=1, le=5, description="Calificación de 1 a 5 estrellas")
    comentario: str = Field(..., max_length=1000, description="Comentario descriptivo del servicio")

class ResenaResponse(BaseModel):
    numero_contrato: str
    calificacion: int
    comentario: str
    fecha: datetime

class NineraCreate(BaseModel):
    nombre_completo: str = Field(..., min_length=2, description="Nombre completo de la niñera")
    foto_url: str = Field(..., min_length=5, description="URL pública de la foto de perfil")
    titulo: str = Field(..., description="Título profesional o rol (ej: Enfermera Pediátrica)")
    descripcion: str = Field(..., max_length=2000, description="Descripción del perfil y experiencia")

class NineraResponse(BaseModel):
    id: UUID
    nombre_completo: str
    foto_url: str
    titulo: str
    descripcion: str
    resenas: List[ResenaResponse]
    creado_en: datetime
