import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("C:\\Users\\Lenovo\\travel-guide\\travel_guide\\travel_guide\\travel-app-b908e-firebase-adminsdk-fbsvc-7f781d1d79.json")


firebase_admin.initialize_app(cred)