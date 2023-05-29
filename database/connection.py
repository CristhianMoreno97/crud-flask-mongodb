from pymongo import MongoClient
from os import getenv
import certifi

class Database:
    def __init__(self):
        self._client = None
        self._db = None

    def connect(self):
        try:
            self._client = MongoClient(getenv("MONGO_URI"), tlsCAFile=certifi.where())
            self._db = self._client[getenv("MONGO_DB")]
            print("Connected to database")
        except Exception as e:
            print(f"Could not connect to database: {str(e)}")

    def close_connection(self):
        if self._client:
            self._client.close()
            print("Connection to database closed")

    def getCollection(self, collection):
        return self._db[collection]