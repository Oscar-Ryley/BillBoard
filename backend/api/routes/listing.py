from flask import Blueprint

listing = Blueprint("listing", __name__)

@listing.route("/listing/<id>")
def listing_route(id):
    """
    Get listings for a specific book and edition

    Response:
    {
        "id": "1", // This is the ISBN
        "title": "Example Listing",
        "description": "This is an example listing.",
        "image": "https://example.com/image.jpg",
        "marketPrize": 120.00,
        prices: [
            {
                "date": "2021-01-01T12:00:00Z",
                "new": 100.00,
                "used": 90.00
                "average": 95.00
            },
            {
                "date": "2021-01-01T12:00:00Z",
                "new": 100.00,
                "used": 90.00
                "average": 95.00
            }
        ],
        "offers": [
            {
                "id": "1",
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
        ],
        "editions": [
            2,
            3,
            5
        ]
    }
    """
    ...