from flask_restful import Resource
from webargs.flaskparser import use_args

from src.schemas.log_schemas import *
from src.services.log_services import *
from src.extensions.api import api

class LogRoutes(Resource):
    @use_args(argmap=QueryLogSchema, location="json")
    def post(self, args):
        """
        parameters:
          - name: body
            description: Payload JSON com os filtros de busca desejados.
            in: body
            required: true
            schema:
              $ref: "#/definitions/QueryLog"

        responses:
          201:
            description: Uma lista com todos os logs que obedecem aos filtros.
            schema:
              type: array
              items:
                $ref: "#/definitions/ResponseLog"
          404:
            description: Nenhum log atende aos filtros descritos.
            schema:
              type: object
            properties:
              status_code:
                type: int
              error:
                type: string
              detail:
                type: string
        """
        return ResponseLogSchema.dump(list_logs(args))


api.add_resource(LogRoutes, "/logs")