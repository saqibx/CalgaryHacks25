import gridfs
from flask import Flask
from pymongo import MongoClient
from config import Config  # Import config settings


# Setup MongoDB Connection
client = MongoClient(Config.MONGO_URI)
db = client["userbase"]

# Collections
users_collection = db['users']
uploads_collection = db['uploads']

# GridFS for storing files
fs = gridfs.GridFS(db)
