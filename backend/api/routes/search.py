from flask import Blueprint, request
from .classes import Listing
from re import findall

search = Blueprint("search", __name__)

@search.route("/search")
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

    query: str = request.args.get("query")
    
    return {
        "results": [
            listing.to_json()
            for listing in Listing.all()
            if (
                query.lower() in listing.title.lower() or \
                query.lower() in listing.description.lower() or \
                findall(query.lower(), listing.title.lower()) or \
                findall(query.lower(), listing.description.lower())
            )
        ]
    }