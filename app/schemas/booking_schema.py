from pydantic import BaseModel, Field, field_validator
from typing import List
from datetime import date, time, datetime
from uuid import UUID
from app.models.booking import TipoServicio

class NinoCreate(BaseModel):
    edad: int = Field(..., gt=0, lt=18, description="Edad del niño")
    condiciones_especiales: str = Field(default="", description="Cualesquier condiciones especiales o alergias")

class PadreCreate(BaseModel):
    nombre_completo: str = Field(..., min_length=2, description="Nombre completo del padre o tutor")
    numero_documento: str = Field(..., min_length=5, description="Número de documento de identidad")
    telefono_whatsapp: str = Field(..., pattern=r"^\+?\d{10,15}$", description="Número de WhatsApp (el + es opcional)")

class DetallesServicioCreate(BaseModel):
    fecha_inicio: date
    hora_inicio: time
    tipo: TipoServicio

class ReservaCreate(BaseModel):
    padre: PadreCreate
    detalles_servicio: DetallesServicioCreate
    ninos: List[NinoCreate] = Field(..., min_length=1, description="Se requiere al menos un niño marcado en la reserva")

class ReservaResponse(BaseModel):
    id: UUID
    padre: PadreCreate
    detalles_servicio: DetallesServicioCreate
    ninos: List[NinoCreate]
    creado_en: datetime
