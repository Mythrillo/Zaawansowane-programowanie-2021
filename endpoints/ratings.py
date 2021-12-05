from csv import reader
from typing import List

from flask_restful import Resource

from models.Rating import Rating


class Ratings(Resource):

    def get(self) -> List[dict]:

        ratings = []
        with open("data/ratings.csv", encoding="utf8") as csv_file:
            csv_reader = reader(csv_file)
            header = next(csv_reader)

            if header is not None:
                for row in csv_reader:
                    ratings.append(Rating(
                        row[0],
                        row[1],
                        row[2],
                        row[3]
                    ))

        return [rating.__dict__() for rating in ratings]
