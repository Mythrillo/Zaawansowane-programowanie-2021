from flask import Flask
from flask_restful import Api

from endpoints.movies import Movies
from endpoints.links import Links
from endpoints.ratings import Ratings
from endpoints.tags import Tags


app = Flask(__name__)
api = Api(app)


api.add_resource(Movies, "/movies")
api.add_resource(Tags, "/tags")
api.add_resource(Ratings, "/ratings")
api.add_resource(Links, "/links")

if __name__ == "__main__":
    app.run(debug=True)
