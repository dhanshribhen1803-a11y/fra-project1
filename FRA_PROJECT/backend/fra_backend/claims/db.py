from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["fra_db"]
claims_collection = db["claims"]
