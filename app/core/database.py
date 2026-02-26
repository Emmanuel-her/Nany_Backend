import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb+srv://Edwin:32278022Sa@chatapp.4bqewtd.mongodb.net/?appName=chatApp")
client = AsyncIOMotorClient(MONGODB_URI)

def get_database():
    """Dependency to get the database instance"""
    return client.get_default_database("nana_db")
