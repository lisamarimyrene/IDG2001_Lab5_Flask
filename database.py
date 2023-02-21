from pymongo import MongoClient
import os

client = MongoClient(os.getenv("mongodb://mongo:7ttkSOoWJ9zRZ2NGdtAm@containers-us-west-53.railway.app:7181"))

db = client.get_default_database()

