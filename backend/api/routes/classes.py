from __future__ import annotations

from pymongo import MongoClient
from typing import List, Dict, Union
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
    bookID: str
    title: str
    description: str
    price: float # Maket price
    image: str
    date: datetime
    offers: List[Offer]
    prices: List[Dict[str, Union[datetime, float]]]
    editions: List[str]


    def __init__(self, book_id: int):
        listings = listings.find_one({"bookID": book_id})

        if not listings:
            raise BookNotFound(f"Book with ID {book_id} not found.")
        
        # Change offers into Offer objects
        for offer in listings["offers"]:
            offer = Offer.from_listing(self, offer["seller"]) # time complexity O(n^2) but this is a hackathon so who cares, it looks nice
        
        self.__dict__.update(dict(listings)) # Convert all the keys in the dictionary to attributes of the class

    @property
    def average_price(self):
        return {
            "new": sum([x["new"] for x in self.prices]) / len(self.prices),
            "used": sum([x["used"] for x in self.prices]) / len(self.prices),
            "average": (sum([x["new"] for x in self.prices]) + sum([x["used"] for x in self.prices])) / (len(self.prices) * 2)  
        }
    
    def add_offer(self, offer: Offer) -> None:
        listings.update_one({"bookID": self.bookID}, {"$push": {"offers": offer.to_json()}})

    def to_json(self):
        return {
            "id": self.bookID,
            "title": self.title,
            "description": self.description,
            "image": self.image,
            "marketPrize": self.price,
            "prices": self.prices,
            "offers": self.offers,
            "editions": self.editions
        }


class Offer:
    bookID: str
    price: float
    condition: Condition
    notes: str
    location: str
    date: datetime
    seller: Dict[str, Union[int, str]]

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    @staticmethod
    def from_listing(listing: Listing, seller: int) -> Offer:
        for offer in listing.offers:
            if offer["seller"] == seller:
                offer["condition"] = Condition(offer["condition"])
                return Offer(**offer)
            
        raise OfferNotFound(f"Offer with ID {seller} not found.")
    
    @staticmethod
    def new(
        listing: Listing, 
        *, 
        price: float, 
        condition: Condition, 
        notes: str, 
        location: str, 
        date: datetime
    ) -> Offer:
        return Offer(
            bookID=listing.bookID,
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