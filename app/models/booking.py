from enum import Enum
from typing import List
from uuid import UUID, uuid4
from dataclasses import dataclass, field
from datetime import date, time, datetime, timezone

class TipoServicio(str, Enum):
    expreso = "expreso"
    estandar = "estandar"
    premium = "premium"

@dataclass
class Padre:
    nombre_completo: str
    numero_documento: str
    telefono_whatsapp: str

@dataclass
class Nino:
    edad: int
    condiciones_especiales: str

@dataclass
class DetallesServicio:
    fecha_inicio: date
    hora_inicio: time
    tipo: TipoServicio
    estado: str = "pendiente"

@dataclass
class Reserva:
    padre: Padre
    detalles_servicio: DetallesServicio
    ninos: List[Nino]
    id: UUID = field(default_factory=uuid4)
    creado_en: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
