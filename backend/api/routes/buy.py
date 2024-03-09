from flask import Blueprint, request
from .classes import Listing, Offer

buy = Blueprint("buy", __name__)

@buy.route("/buy", methods=["POST"])
def buy_route():
    """
    Delets the book to the db

    Request:
    {
        "id": "1", // ISBN
        "seller": 1
    }
    Response:
    {
        "success": true
    }
    """
    id = request.json["id"]
    seller = request.json["seller"]

    listing = Listing(id)
    listing.remove_offer(
        Offer.from_listing(
            listing,
            seller
        )
    )
    return {"success": True}