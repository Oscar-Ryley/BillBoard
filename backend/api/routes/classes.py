from __future__ import annotations

from pymongo import MongoClient, bson
import json
from enum import Enum
from datetime import datetime

with open("backend/config.json") as f:
    data = json.load(f)
    MONGO_DB = data["mongodb"]

client = MongoClient(MONGO_DB)
db = client["hackathon"]
listings = db["listings"]

class BookNotFound(Exception):
    pass

class OfferNotFound(Exception):
    pass

class Condition(Enum):
    NEW = "new"
    USED = "used"

class Listing:

    def __init__(self, book_id: int, book_version: int):
        listings = listings.find_one({"bookID": book_id, "editionID": book_version})

        if not listings:
            raise BookNotFound(f"Book with ID {book_id} and version {book_version} not found.")
        
        self.__dict__.update(dict(listings)) # Convert all the keys in the dictionary to attributes of the class

    @property
    def average_price(self):
        return {
            "new": sum([x["new"] for x in self.prices]) / len(self.prices),
            "used": sum([x["used"] for x in self.prices]) / len(self.prices),
            "average": (sum([x["new"] for x in self.prices]) + sum([x["used"] for x in self.prices])) / (len(self.prices) * 2)  
        }
    
    def add_offer(self, offer: Offer) -> None:
        listings.update_one({"_id": self._id}, {"$push": {"offers": offer.to_json()}})


class Offer:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    @staticmethod
    def from_listing(listing: Listing, id: bson.ObjectId):
        for offer in listing.offers:
            if offer["_id"] == id:
                return Offer(**offer)
            
        raise OfferNotFound(f"Offer with ID {id} not found.")
    
    @staticmethod
    def new(
        listing: Listing, 
        *, 
        price: float, 
        condition: Condition, 
        notes: str, 
        location: str, 
        date: datetime
    ) -> None:
        return Offer(
            bookID=listing.bookID,
            editionID=listing.editionID,
            price=price,
            condition=condition,
            notes=notes,
            location=location,
            date=date
        )
    
    def to_json(self):
        return {
            "price": self.price,
            "condition": self.condition.value,
            "notes": self.notes,
            "location": self.location,
            "date": self.date
        }