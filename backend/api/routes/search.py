from flask import Blueprint

search = Blueprint("search", __name__)

@search.route("/search?query=<query>")
def search_route():
    """
    Response:
    {
        "results": [
            {
                "id": 1,
                "editionID": 1,
                "title": "Example Listing",
                "description": "This is an example listing.",
                "price": 100.00,
                "image": "https://example.com/image.jpg",
                "date": "2021-01-01T12:00:00Z"
            },

            {
                "id": 2,
                "editionID": 2,
                "title": "Example Listing 2",
                "description": "This is another example listing.",
                "price": 90.00,
                "image": "https://example.com/image2.jpg",
                "date": "2021-01-01T12:00:00Z"
            }
        ]
    }
    """
    ...