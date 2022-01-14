from flask_restful import Resource
from flask import Response
from flask import render_template


class Index(Resource):
    
    def get(self):
        return Response(response=render_template("index.html"))
