#!/usr/bin/env python3
import datetime
from pymongo import MongoClient
from src.config import config


class DatabaseHandler(MongoClient):
    def __init__(self):
        url = config.AZURE_DATABASE_URL
        super(DatabaseHandler, self).__init__(url)

    def authenticate(self, db_name="ey"):
        username = config.AZURE_DATABASE_USER
        password = config.AZURE_DATABASE_PASSWORD
        db = getattr(self, db_name)
        db.authenticate(name = username, password = password)
        self.used_db = db
        return db

    def addDocument(self, collection, document):
        if not isinstance(document, dict):
            raise TypeError("Database Handler: expected type dict, got {}".format(type(document)))
        collection = getattr(self.used_db, collection)
        return collection.insert_one(document).inserted_id

    def addMultipleDocuments(self, collection, documents):
        if not isinstance(documents, list):
            raise TypeError("Database Handler: expected type list, got {}".format(type(document)))
        collection = getattr(self.used_db, collection)
        return collection.insert_many(documents).inserted_ids


if __name__ == "__main__":
    handler = DatabaseHandler()
    db = handler.authenticate()
    test_object = [{"test": "yes",
                   "working": "ok",
                   "id": 3,
                   "multipleDocuments": 1,
                   "date": datetime.datetime.utcnow()},
                   {"test": "yes",
                   "working": "ok",
                   "id": 4,
                   "multipleDocuments": 1,
                   "date": datetime.datetime.utcnow()}
    ]

    handler.addDocument("test_conn", {"singleDocument": 1})
    print("Added single document")
    handler.addMultipleDocuments("test_conn", test_object)
    print("Added list of documents")
    print("Demo working ok!")
    print("Exitting")

