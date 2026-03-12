import urllib.request
import json

data = {
    "nombre_completo": "Maria Gomez",
    "foto_url": "https://example.com/foto-maria.jpg",
    "titulo": "Enfermera Pediatrica",
    "descripcion": "10 años trabajando con bebes."
}

req = urllib.request.Request(
    'http://localhost:8080/nannies', 
    data=json.dumps(data).encode('utf-8'), 
    headers={'Content-Type': 'application/json'}
)

try:
    with urllib.request.urlopen(req) as f:
        print("Status", f.status)
        resp = f.read().decode('utf-8')
        print("Response", resp)
        
        # Guardar ID para el siguiente paso
        ninera_id = json.loads(resp)["id"]
        
        # Agregar reseña
        review_data = {
            "numero_contrato": "CTR-2026-001",
            "calificacion": 5,
            "comentario": "Excelente servicio, muy puntual y profesional."
        }
        
        req_review = urllib.request.Request(
            f'http://localhost:8080/nannies/{ninera_id}/reviews', 
            data=json.dumps(review_data).encode('utf-8'), 
            headers={'Content-Type': 'application/json'}
        )
        with urllib.request.urlopen(req_review) as fr:
            print("Review Status", fr.status)
            print("Review Response", fr.read().decode('utf-8'))
            
except urllib.error.HTTPError as e:
    print("HTTPError", e.code)
    print(e.read().decode('utf-8'))
except Exception as e:
    print("Error", e)
