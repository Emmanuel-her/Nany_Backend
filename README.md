# Prueba Técnica Nequi - Booking API Clean Architecture

## 📋 Requisitos Previos
- Python 3.11+
- MongoDB 
- Docker (Opcional)

## 🚀 Cómo correr el proyecto localmente

1. Crear un entorno virtual e instalar las dependencias:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. Asegúrate de tener MongoDB corriendo (por defecto en `mongodb://localhost:27017`). Puedes configurar la URI en un archivo `.env` o exportando la variable `MONGODB_URI`.

3. Iniciar el servidor:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
La documentación interactiva de Swagger estará disponible en: http://localhost:8000/docs

## 🐳 Cómo correr el proyecto con Docker

1. Construir la imagen:
```bash
docker build -t booking-api .
```

2. Ejecutar el contenedor (asegurando conexión a base de datos externa o host.docker.internal):
```bash
docker run -p 8000:8000 -e MONGODB_URI="mongodb://host.docker.internal:27017/nana_db" booking-api
```

---

## 📝 Ejemplos JSON

### Request (POST /bookings)
```json
{
  "padre": {
    "nombre_completo": "María González",
    "numero_documento": "123456789",
    "telefono_whatsapp": "+573001234567"
  },
  "detalles_servicio": {
    "fecha_inicio": "2026-03-15",
    "hora_inicio": "14:30:00",
    "tipo": "expreso"
  },
  "ninos": [
    {
      "edad": 4,
      "condiciones_especiales": "Alergia al maní"
    }
  ]
}
```

### Response (POST /bookings - 201 Created)
```json
{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "padre": {
    "nombre_completo": "María González",
    "numero_documento": "123456789",
    "telefono_whatsapp": "+573001234567"
  },
  "detalles_servicio": {
    "fecha_inicio": "2026-03-15",
    "hora_inicio": "14:30:00",
    "tipo": "expreso"
  },
  "ninos": [
    {
      "edad": 4,
      "condiciones_especiales": "Alergia al maní"
    }
  ],
  "creado_en": "2026-02-26T16:30:00Z"
}
```

### Response (GET /bookings - 200 OK)
```json
[
  {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "padre": {
      "nombre_completo": "María González",
      "numero_documento": "123456789",
      "telefono_whatsapp": "+573001234567"
    },
    "detalles_servicio": {
      "fecha_inicio": "2026-03-15",
      "hora_inicio": "14:30:00",
      "tipo": "expreso"
    },
    "ninos": [
      {
        "edad": 4,
        "condiciones_especiales": "Alergia al maní"
      }
    ],
    "creado_en": "2026-02-26T16:30:00Z"
  }
]
```

## 🏗️ Estructura del Proyecto

El proyecto sigue una estricta **Clean Architecture**, con total desacoplamiento de capas:

- **Domain Layer**: `app/models/booking.py` - Entidades puras y Value Objects. No depende de Pydantic, Mongo, ni FastAPI.
- **Port**: `app/repositories/booking_repository.py` - Interfaz para la persistencia (Inversión de dependencias).
- **Adapter**: `app/repositories/mongo_booking_repository.py` - Implementación con Motor para MongoDB.
- **Application Layer**: `app/services/create_booking_service.py` - Caso de uso o capa de servicio. Aplica inyección de dependencias y lógica de negocio pura.
- **Presentation Layer**: `app/api/bookings.py` y `app/schemas/booking_schema.py` - Routers y DTOs robustos con Pydantic V2. Validaciones estrictas.
