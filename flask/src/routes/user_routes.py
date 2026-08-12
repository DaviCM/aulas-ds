from flask_restful import Resource
from webargs.flaskparser import use_args
from marshmallow import fields

from src.schemas.user_schemas import *
from src.services.user_services import *
from src.extensions.api import api

class UserRoutes(Resource):
    @use_args(argmap=CreateUserSchema, location="json")
    def post(self, args):
        return ResponseUserSchema.dump(create_user(args)), 201


    @use_args(argmap=UpdateUserSchema, location="json")
    def patch(self, args):
        return ResponseUserSchema.dump(update_user(args)), 200


    @use_args(argmap={"id": fields.Int(required=True)}, location="query")
    def delete(self, args):
        delete_user(id=args)
        return 204



class UserLogin(Resource):
    @use_args(argmap=LoginUserSchema, location="json")
    def post(self, args):
        return ResponseUserSchema.dump(login(args["email"], args["password"])), 200



api.add_resource(UserRoutes, "/users")
api.add_resource(UserLogin, "/auth")