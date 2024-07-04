from pymongo import MongoClient

client= MongoClient()

db= client.database

collection_name = db["collection_name"]

