from abc import ABC, abstractmethod
import firebase_admin
from firebase_admin import messaging

class NotificationService(ABC):
    @abstractmethod
    def enviar_notificacion(self, titulo: str, cuerpo: str, topic: str = "reservas", token: str = None) -> str:
        """Envia una notificacion push."""
        pass


class FirebaseNotificationService(NotificationService):
    def enviar_notificacion(self, titulo: str, cuerpo: str, topic: str = "reservas", token: str = None) -> str:
        # Asegurarse que firebase esta inicializado
        if not firebase_admin._apps:
            print("Firebase APP no ha sido inicializada. Saltando envio de notificacion.")
            return ""
            
        try:
            # Puedes enviar al topic o un token especifico
            if token:
                mensaje = messaging.Message(
                    notification=messaging.Notification(
                        title=titulo,
                        body=cuerpo,
                    ),
                    token=token,
                )
            else:
                mensaje = messaging.Message(
                    notification=messaging.Notification(
                        title=titulo,
                        body=cuerpo,
                    ),
                    topic=topic,
                )
                
            response = messaging.send(mensaje)
            print(f"Notificacion enviada exitosamente: {response}")
            return response
            
        except Exception as e:
            print(f"Error enviando notificacion Firebase: {e}")
            return ""
