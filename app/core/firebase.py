import os
import firebase_admin
from firebase_admin import credentials

def init_firebase():
    # Evitar inicializar multiples veces en modo reload
    if not firebase_admin._apps:
        cred_path = os.getenv("FIREBASE_CREDENTIALS_PATH")
        if cred_path and os.path.exists(cred_path):
            cred = credentials.Certificate(cred_path)
            firebase_admin.initialize_app(cred)
            print("Firebase initialized successfully")
        else:
            print(f"Warning: Firebase credentials not found at {cred_path}")
