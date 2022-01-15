from flask import Response
from flask_restful import Resource
from flask_restful import reqparse
import werkzeug

from logic.detection import detect_people


class PersonDetection(Resource):
    def post(self) -> Response:
        parser = reqparse.RequestParser()
        parser.add_argument("file", type=werkzeug.datastructures.FileStorage, location='files')
        args = parser.parse_args()
        try:
            return detect_people(args["file"])
        except Exception:
            return Response("something went wrong", 500)
