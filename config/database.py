from pymongo import MongoClient

client= MongoClient()

db= client.database

collection_name = db["todo_collection"]

