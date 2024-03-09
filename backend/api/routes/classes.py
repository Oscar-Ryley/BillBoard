from __future__ import annotations

from pymongo import MongoClient
from typing import List, Dict, Union
import json
from enum import Enum
from datetime import datetime

with open("config.json") as f:
    data = json.load(f)
    MONGO_DB = data["mongodb"]

client = MongoClient(MONGO_DB)
db = client["hackathon"]
LISTINGS = db["listings"]

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
        listings = LISTINGS.find_one({"bookID": str(book_id)})

        if listings is None:
            raise BookNotFound(f"Book with ID {book_id} not found.")
        
        for k, v in dict(listings).items():
            if k == "offers": k="_offers"
            setattr(self, k, v)

        # Change offers into Offer objects
        # for offer in self.offers:
        #     offer = Offer.new(**offer, bookID=book_id)

        # print(self.offers)
        # self.__dict__.update(**dict(listings)) # Convert all the keys in the dictionary to attributes of the class

    @property
    def offers(self):
        return [Offer.new(**offer, bookID=self.bookID) for offer in self._offers]

    @property
    def average_price(self):
        return {
            "new": sum([x["new"] for x in self.prices]) / len(self.prices),
            "used": sum([x["used"] for x in self.prices]) / len(self.prices),
            "average": (sum([x["new"] for x in self.prices]) + sum([x["used"] for x in self.prices])) / (len(self.prices) * 2)  
        }
    
    @staticmethod
    def all() -> List[Listing]:
        return [Listing(x["bookID"]) for x in LISTINGS.find()]
    
    @staticmethod
    def search(query: str) -> List[Listing]:
        return [Listing(x["bookID"]) for x in LISTINGS.find({"title": {"$regex": query}})]
    
    @staticmethod
    def get_editions(book_id: str) -> List[Listing]:
        """Fetch data about the one book, find its editions, then return all those listings including the same book"""
        first = Listing(book_id)
        l = [Listing(x) for x in first.editions]
        if not first.bookID in [book.bookID for book in l]:
            l.append(first)
        # Let me explain why I do this lol. Initially I had thought a book may have an additional list
        # containing alternative ISBNs of editions. Now I realise that list may make sense to also
        # include its own ID. I want capabilities for both, so I'm doing this.

        return l

    
    def add_offer(self, offer: Offer) -> None:
        LISTINGS.update_one({"bookID": self.bookID}, {"$push": {"offers": offer.to_json()}})

    def remove_offer(self, offer: Offer) -> None:
        # for off in self.offers:
        #     if off.seller["id"] == offer.seller["id"]:
        #         del off

        LISTINGS.update_one({"bookID": self.bookID}, {"$set": {"offers": [o.to_json() for o in self.offers if o.seller["id"] != offer.seller["id"]]}})

    def to_json(self):
        return {
            "id": self.bookID,
            "title": self.title,
            "description": self.description,
            "image": self.image,
            "marketPrize": self.price,
            "prices": self.prices,
            "offers": [offer.to_json() for offer in self.offers],
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
            if offer.seller["id"] == seller:
                offer.condition = Condition(offer.condition)
                return offer
            
        raise OfferNotFound(f"Offer with ID {seller} not found.")
    
    @staticmethod
    def new(
        bookID: str, 
        *, 
        price: float, 
        condition: Condition, 
        notes: str, 
        location: str, 
        date: datetime,
        seller: Dict[str, Union[int, str]],
        **_
    ) -> Offer:
        return Offer(
            bookID=bookID,
            price=price,
            condition=condition,
            notes=notes,
            location=location,
            date=date,
            seller=seller
        )
    
    def to_json(self):
        return {
            "price": self.price,
            "condition": self.condition.value if hasattr(self.condition, "value") else self.condition,
            "notes": self.notes,
            "location": self.location,
            "date": self.date,
            "seller": self.seller
        }