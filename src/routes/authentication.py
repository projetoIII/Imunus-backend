from flask import request
from flask_restplus import Resource
from src.routes import authentication_api as api
from src.routes.endpoints import Endpoints

@api.route(Endpoints.authentication)
class Login(Resource):
    @api.doc('Rota de login')
    def post(self):
        body = request.json
        print(body)