from flask import Blueprint

editions = Blueprint("editions", __name__)

@editions.route("/editions/<id>")
def editions_route(id):
    """
    Get all editions of a book using its "editions" fields
    """
    ...