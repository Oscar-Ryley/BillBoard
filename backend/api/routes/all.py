from flask import Blueprint
from .classes import Listing

all = Blueprint("all", __name__)

@all.route("/all")
def all_route():
    """
    Get all listings
    """
    return {
        "results": [listing.to_json() for listing in Listing.all()]
    }