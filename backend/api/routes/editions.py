from flask import Blueprint
from .classes import Listing

editions = Blueprint("editions", __name__)

@editions.route("/editions/<id>")
def editions_route(id):
    """
    Get all editions of a book using its "editions" fields
    """
    return {
        "results": Listing.get_editions(id)
    }