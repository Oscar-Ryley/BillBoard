from flask import Blueprint

create = Blueprint("create", __name__)

@create.route("/create", methods=["POST"])
def create_route():
    """
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
        "id": 1
    }
    """
    ...