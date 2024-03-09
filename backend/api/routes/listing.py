from flask import Blueprint

listing = Blueprint("listing", __name__)

@listing.route("/listing/<id>")
def listing_route(id):
    """
    Response:
    {
        "id": 1,
        "title": "Example Listing",
        "description": "This is an example listing.",
        "image": "https://example.com/image.jpg",
        "offers": [
            {
                "id": 1,
                "price": 100.00,
                "date": "2021-01-01T12:00:00Z",
                "seller": {
                    "id": 1,
                    "username": "example"
                },
                "conition": "new"
                "notes": None,
                "location": "Sheffield"
            },
            {
                "id": 2,
                "price": 90.00,
                "date": "2021-01-01T12:00:00Z",
                "seller": {
                    "id": 2,
                    "username": "example2"
                },
                "conition": "used"
                "notes": "This is a note.",
                "location": "Newcastle"
            }
        ]
    }
    """
    ...