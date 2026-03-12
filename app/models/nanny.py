from typing import List, Optional
from uuid import UUID, uuid4
from dataclasses import dataclass, field
from datetime import datetime, timezone

@dataclass
class Resena:
    numero_contrato: str
    calificacion: int
    comentario: str
    fecha: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

@dataclass
class Ninera:
    nombre_completo: str
    foto_url: str
    titulo: str
    descripcion: str
    resenas: List[Resena] = field(default_factory=list)
    id: UUID = field(default_factory=uuid4)
    creado_en: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
