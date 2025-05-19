import os

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()

def db_client():
 
    CONNECTION_STRING = os.environ.get("CONNECTION_STRING")
 
    client = MongoClient(CONNECTION_STRING, server_api=ServerApi('1'))

    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    return client
        
if __name__ == "__main__":   
  
   client = db_client()
   db = client["linkshortener"]
   links = db["links"]
