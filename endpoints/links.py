from csv import reader
from typing import List

from flask_restful import Resource

from models.Link import Link


class Links(Resource):

    def get(self) -> List[dict]:

        links = []
        with open("data/links.csv", encoding="utf8") as csv_file:
            csv_reader = reader(csv_file)
            header = next(csv_reader)

            if header is not None:
                for row in csv_reader:
                    links.append(Link(
                        row[0],
                        row[1],
                        row[2]
                    ))

        return [link.__dict__() for link in links]
