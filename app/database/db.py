import pathlib
import firebase_admin
import pyrebase
from firebase_admin import credentials, firestore
from app.config import get_settings

BASE_DIR = pathlib.Path(__file__).resolve().parent

settings = get_settings()
connect_file = "npaas-db.json"

FIRE_DB_CREDENTIALS = BASE_DIR / "restricted" / connect_file

FIRE_CONFIG = {
    "apiKey": settings.db_client_key,
    "authDomain": settings.db_client_domain,
    "projectId": settings.db_client_id,
    "storageBucket": settings.db_client_store,
    "messagingSenderId": settings.db_client_push,
    "appId": settings.db_client_app,
    "measurementId": settings.db_client_measure,
    "databaseURL": ""
}


def get_session():
    if not firebase_admin._apps:
        cred = credentials.Certificate(FIRE_DB_CREDENTIALS)
        firebase_admin.initialize_app(cred)
    settings.db = firestore.client()
    firebase = pyrebase.initialize_app(FIRE_CONFIG)
    return firebase
