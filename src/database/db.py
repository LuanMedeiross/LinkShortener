import os

from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()

def get_db():
 
    CONNECTION_STRING = os.environ.get("CONNECTION_STRING")
 
    client = MongoClient(CONNECTION_STRING, server_api=ServerApi('1'))

    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    db = client["linkshortener"]

    return db
        
