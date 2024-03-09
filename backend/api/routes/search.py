from flask import Blueprint, request
from .classes import Listing

search = Blueprint("search", __name__)

@search.route("/search?query=<query>")
def search_route():
    """
    Get all listings that match the query

    Response:
    {
        "results": [
            {
                "id": 1,
                "title": "Example Listing",
                "description": "This is an example listing.",
                "price": 100.00,
                "image": "https://example.com/image.jpg",
                "date": "2021-01-01T12:00:00Z"
            },

            {
                "id": 2,
                "title": "Example Listing 2",
                "description": "This is another example listing.",
                "price": 90.00,
                "image": "https://example.com/image2.jpg",
                "date": "2021-01-01T12:00:00Z"
            }
        ]
    }
    """

    query = request.args.get("query")
    return {
        "results": Listing.search(query)
    }