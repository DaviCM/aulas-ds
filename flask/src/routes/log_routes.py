from flask_restful import Resource
from webargs.flaskparser import use_args

from src.schemas.log_schemas import *
from src.services.log_services import *
from src.extensions.api import api

class LogRoutes(Resource):
    @use_args(argmap=QueryLogSchema, location="json")
    def post(self, args):
        """
        """
        return ResponseLogSchema.dump(list_logs(args))


api.add_resource(LogRoutes, "/logs")