#for local Database
# from pymongo import MongoClient

# client = MongoClient("mongodb://localhost:27017/")

# try:
#     client.admin.command("ping")
#     print("MongoDB is connected!")
#     db = client["courseplatform"]
#     courses_collection = db["courses"]

# except Exception as e:
#     print("Connection failed:", e)
#     courses_collection = None


#for database cloud 
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "url"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client["courseplatform"]
courses_collection = db["courses"]
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)