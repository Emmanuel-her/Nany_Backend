import urllib.request
import json

url = "http://127.0.0.1:8000/bookings"
payload = {
    "padre": {
        "nombre_completo": "Carlos miguel",
        "numero_documento": "102326582",
        "telefono_whatsapp": "3053762987"
    },
    "detalles_servicio": {
        "fecha_inicio": "2026-02-27",
        "hora_inicio": "21:52:40",
        "tipo": "expreso"
    },
    "ninos": [
        {
            "edad": 8,
            "condiciones_especiales": "Esta en sillas de ruedas"
        }
    ]
}

data = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(url, data=data, method='POST')
req.add_header('Content-Type', 'application/json')
req.add_header('accept', 'application/json')

try:
    with urllib.request.urlopen(req) as f:
        print(f"Status Code: {f.status}")
        print(f"Response: {f.read().decode('utf-8')}")
except Exception as e:
    print(f"Error: {e}")
    if hasattr(e, 'read'):
        print(f"Error Response: {e.read().decode('utf-8')}")
