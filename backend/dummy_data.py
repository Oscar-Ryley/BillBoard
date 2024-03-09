from pymongo import MongoClient
import json
from datetime import datetime

with open("config.json") as f:
    data = json.load(f)
    MONGO_DB = data["mongodb"]

client = MongoClient(MONGO_DB)
db = client["hackathon"]
listings = db["listings"]

if __name__ == "__main__":
    listings.insert_one({
        "bookID": 9780262367509,
        "editionID": 4,
        "title": "Introduction to Algorithms, Fourth Edition",
        "description": "A comprehensive update of the leading algorithms text, with new material on matchings in bipartite graphs, online algorithms, machine learning, and other topics.",
        "price": 150.00,
        "image": "https://mit-press-us.imgix.net/covers/9780262046305.jpg",
        "date": datetime.now(),
        "offers": [
            {
                "price": 60.00,
                "date": datetime.now(),
                "seller": 1,
                "condition": "new",
                "notes": None,
                "location": "Sheffield"
            }
        ],
        "prices": [
            {
                "date": datetime.now(),
                "new": 50.00,
                "used": 35.00,
                "average": 40.23
            }
        ],
        # "editions": [2, 3]  # If this is present, there MUST be corresponding listings in the db with the same version and book number
    })
    # 
    # Bring some variations into the datetime by constructing it yourself eg
    # datetime(year, month, day, hour, minute, second, microsecond)
    # Example: datetime(2021, 1, 1, 12, 0, 0, 0)
