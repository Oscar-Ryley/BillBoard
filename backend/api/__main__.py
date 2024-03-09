from flask import Flask
from api.routes import listing, search, create

app = Flask(__name__)
app.register_blueprint(listing)
app.register_blueprint(search)
app.register_blueprint(create)

if __name__ == "__main__":
    app.run()