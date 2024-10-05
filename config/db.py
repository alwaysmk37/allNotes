from pymongo import MongoClient

MONGO_URI = "mongodb+srv://bhaiyaji:bhaiyaji@appdev.cxfgi.mongodb.net/"
conn = MongoClient(MONGO_URI).your_database_name  # Specify your database name
