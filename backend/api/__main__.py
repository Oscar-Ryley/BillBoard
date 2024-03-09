from flask import Flask
from api.routes import listing, search, create, buy, editions, all

app = Flask(__name__)
app.register_blueprint(listing)
app.register_blueprint(search)
app.register_blueprint(create)
app.register_blueprint(buy)
app.register_blueprint(editions)
app.register_blueprint(all)

if __name__ == "__main__":
    print(app.url_map)
    app.run()