from pymongo import MongoClient
import json
from datetime import datetime

with open("backend/config.json") as f:
    data = json.load(f)
    MONGO_DB = data["mongodb"]

client = MongoClient(MONGO_DB)
db = client["hackathon"]
listings = db["listings"]

if __name__ == "__main__":

    # Add a listing like this:
    # listings.insert_one({
    #     "bookID": 1,
    #     "editionID": 1,
    #     "title": "Example Listing",
    #     "description": "This is an example listing.",
    #     "price": 100.00,
    #     "image": "https://example.com/image.jpg",
    #     "date": datetime.now(),
    #     "offers": [
    #         {
    #             "price": 100.00,
    #             "date": datetime.now(),
    #             "seller": 1,
    #             "condition": "new",
    #             "notes": None,
    #             "location": "Sheffield"
    #         },
    #         {
    #             "price": 90.00,
    #             "date": datetime.now(),
    #             "seller": 2,
    #             "condition": "used",
    #             "notes": "This is a note.",
    #             "location": "Newcastle"
    #         }
    #     ],
    #     "prices": [
    #         {
    #             "date": datetime.now(),
    #             "new": 100.00,
    #             "used": 90.00,
    #             "average": 95.00
    #         },
    #         {
    #             "date": datetime.now(),
    #             "new": 100.00,
    #             "used": 90.00,
    #             "average": 95.00
    #         }
    #     ],
    #     "editions": [2, 3] If this is present, there MUST be corresponding listings in the db with the same version and book number
    # })
    # 
    # Bring some variations into the datetime by constructing it yourself eg
    # datetime(year, month, day, hour, minute, second, microsecond)
    # Example: datetime(2021, 1, 1, 12, 0, 0, 0)