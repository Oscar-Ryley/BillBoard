from flask import Flask
from flask_cors import CORS
from api.routes import listing, search, create, buy, editions, all

app = Flask(__name__)
app.register_blueprint(listing)
app.register_blueprint(search)
app.register_blueprint(create)
app.register_blueprint(buy)
app.register_blueprint(editions)
app.register_blueprint(all)

CORS(app)

if __name__ == "__main__":
    app.run()
