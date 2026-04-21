from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

try:
    client.admin.command("ping")
    print("MongoDB is connected!")
    db = client["courseplatform"]
    courses_collection = db["courses"]

except Exception as e:
    print("Connection failed:", e)
    courses_collection = None