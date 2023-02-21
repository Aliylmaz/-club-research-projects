from firebase_admin import firestore
import firebase_admin
from firebase_admin import credentials,db
import requests

cred = credentials.Certificate("PythonFirebase.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'your database url'
})
ref=db.reference("/")
response =requests.get("https://api.openweathermap.org/data/2.5/forecast?lat=41.0351&lon=28.9833&appid=your api")
data=response.json()
ref.update({'weather':data})
