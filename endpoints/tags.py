from csv import reader
from typing import List

from flask_restful import Resource

from models.Tag import Tag


class Tags(Resource):

    def get(self) -> List[dict]:

        tags = []
        with open("data/tags.csv", encoding="utf8") as csv_file:
            csv_reader = reader(csv_file)
            header = next(csv_reader)

            if header is not None:
                for row in csv_reader:
                    tags.append(Tag(
                        row[0],
                        row[1],
                        row[2],
                        row[3]
                    ))

        return [tag.__dict__() for tag in tags]
