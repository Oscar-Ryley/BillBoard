from flask import Blueprint

buy = Blueprint("buy", __name__)

@buy.route("/buy/<id>", methods=["POST"])
def buy_route(id):
    """
    Delets the book to the db
    
    Request:
    {
        "id": 1,
        "editionID": 1,
        "seller": 1
    }
    Response:
    {
        "success": true
    }
    """
    ...