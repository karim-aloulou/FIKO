
from datetime import datetime as dt
import os
import pandas as pd
from pymongo import MongoClient
from bson import ObjectId
import time

# Remplacez "nom_db" par le nom de votre base de données et "ma_collection" par le nom de votre collection
os.environ['DB_URI'] = 'mongodb+srv://forsaimmobiliere2023:Azerty123@cluster0.q3tboik.mongodb.net/'
db_uri = os.environ.get('DB_URI')
client = MongoClient(db_uri)
db = client.nom_db
collection = db.ma_collection

csv_file_path = 'crafted_data/ClassifiedFIKO.csv'

while True:
    # Charger les données depuis le fichier CSV
    data = pd.read_csv(csv_file_path)

    # Itérer sur les lignes du DataFrame et insérer chaque document dans MongoDB
    for index, row in data.iterrows():
        query = {
            "openedPrograms": row['Opened Programs'],
            "frameNumber": row['Frame Number'],
            "eyeAspectRatio": row['Eye Aspect Ratio'],
            "mouthAspectRatio": row['Mouth Aspect Ratio'],
            "headTiltDegree": row['Head Tilt Degree'],
            "eyePupil": row['Eye Pupil'],
            "cluster": row['Cluster']
        }

        # Vérifier si le document existe déjà dans la collection
        existing_document = collection.find_one(query)

        if existing_document is None:
            document = {
                "_id": ObjectId(),
                "createdAt": dt.now(),
                "openedPrograms": row['Opened Programs'],
                "frameNumber": row['Frame Number'],
                "eyeAspectRatio": row['Eye Aspect Ratio'],
                "mouthAspectRatio": row['Mouth Aspect Ratio'],
                "headTiltDegree": row['Head Tilt Degree'],
                "eyePupil": row['Eye Pupil'],
                "cluster": row['Cluster']
            }

            collection.insert_one(document)
            #print(f'Nouveau document inséré : {document}')

    #time.sleep(10)  # Attendez 60 secondes avant la prochaine vérification
