from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

mongo_client = os.getenv("MONGO_CLIENT")

# Coneccion a la base de datos local
# db_client = MongoClient().local  # MongoClient is a class that allows

#Base de datos remota
print("Mongo Client: ", mongo_client)
db_client = MongoClient(mongo_client).yeicko

