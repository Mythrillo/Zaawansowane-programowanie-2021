from csv import reader
from typing import List

from flask_restful import Resource

from models.Movie import Movie


class Movies(Resource):

    def get(self) -> List[dict]:

        movies = []
        with open("data/movies.csv", encoding="utf8") as csv_file:
            csv_reader = reader(csv_file)
            header = next(csv_reader)

            if header is not None:
                for row in csv_reader:
                    movies.append(Movie(
                        row[0],
                        row[1],
                        row[2]
                    ))

        return [movie.__dict__() for movie in movies]
