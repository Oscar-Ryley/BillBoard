from flask import Blueprint, request
from .classes import Listing, Offer

create = Blueprint("create", __name__)

@create.route("/create", methods=["POST"])
def create_route():
    """
    Creates a new listing in the db

    Request:
    {
        "bookID": 2,
        "price": 80,
        "condition": "new",
        "notes": None,
        "location": "Sheffield",
        "date": "2021-01-01T12:00:00Z"
        "seller": 1
    }
    Response:
    {
        "success": true
    }
    """
    print(request.json)
    Listing(request.json["bookID"]).add_offer(
        Offer.new(
            **request.json # This is INSANELY insecure especially without authentication. But this is a hackathon. Fuck it we ball.
        )
    )

    return {"success": True}