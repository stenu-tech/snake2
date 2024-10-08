from django.apps import AppConfig
import firebase_admin
from firebase_admin import credentials, initialize_app
import os
import json

class FirebaseTestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'firebase_test'

    def ready(self):
        # Initialize Firebase app only if it has not been initialized already
        if not firebase_admin._apps:
            firebase_credentials = os.getenv('FIREBASE_ADMIN_CREDENTIALS')
            if firebase_credentials:
                try:
                    cred = credentials.Certificate(json.loads(firebase_credentials))
                    initialize_app(cred)
                except json.JSONDecodeError:
                    raise ValueError("FIREBASE_ADMIN_CREDENTIALS environment variable is not a valid JSON string")
            else:
                raise ValueError("FIREBASE_ADMIN_CREDENTIALS environment variable is not set")