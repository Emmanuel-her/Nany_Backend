import urllib.request
import json

data = {
    "numero_contrato": "CTR-2026-001",
    "padre": {
        "nombre_completo": "Ana Suarez",
        "numero_documento": "987654321",
        "telefono_whatsapp": "3019876543"
    },
    "detalles_servicio": {
        "fecha_inicio": "2026-04-01",
        "hora_inicio": "08:00:00",
        "fecha_fin": "2026-04-01",
        "hora_fin": "17:00:00",
        "tipo": "estandar"
    },
    "ninos": [
        {
            "edad": 3,
            "condiciones_especiales": "Alergia al mani"
        }
    ]
}

req = urllib.request.Request(
    'http://localhost:8080/bookings', 
    data=json.dumps(data).encode('utf-8'), 
    headers={'Content-Type': 'application/json'}
)

try:
    with urllib.request.urlopen(req) as f:
        print("Status", f.status)
        print("Response", f.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print("HTTPError", e.code)
    print(e.read().decode('utf-8'))
except Exception as e:
    print("Error", e)
