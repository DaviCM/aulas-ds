from flask_restful import Resource
from webargs.flaskparser import use_args
from marshmallow import fields

from src.schemas.product_schemas import *
from src.services.product_services import *
from src.extensions.api import api

class ProductRoutes(Resource):
    @use_args(argmap=CreateProductSchema, location="json")
    def post(self, args):
        """
        parameters:
          - name: body
            description: Payload JSON com as informações do produto a criar.
            in: body
            required: true
            schema:
              $ref: "#/definitions/CreateProduct"

        responses:
          201:
            description: O produto requisitado foi criado com sucesso.
            schema:
              $ref: "#/definitions/ResponseProduct"
          409:
            description: O produto já está cadastrado.
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
        return ResponseProductSchema.dump(create_product(args))


    @use_args(argmap=QueryProductSchema, location="json")
    def get(self, args):
        """
        parameters:
          - name: body
            description: Payload JSON com os filtros de busca desejados.
            in: body
            required: true
            schema:
              $ref: "#/definitions/QueryProduct"

        responses:
          201:
            description: Uma lista com todos os produtos que obedecem aos filtros.
            schema:
              type: array
              items:
                $ref: "#/definitions/ResponseProduct"
          404:
            description: Nenhum produto atende aos filtros descritos.
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
        return ResponseProductSchema.dump(list_products(args), many=True)


    @use_args(argmap=UpdateProductSchema, location="json")
    def patch(self, args):
        """
        parameters:
          - name: body
            description: Payload JSON com os parâmetros a editar. Parâmetros opcionais.
            in: body
            required: true
            schema:
              $ref: "#/definitions/UpdateProduct"

        responses:
          200:
            description: O produto requisitado foi atualizado com sucesso.
            schema:
              $ref: "#/definitions/ResponseProduct"
          404:
            description: O produto requisitado não foi encontrado.
            schema:
              type: object
            properties:
              status_code:
                type: int
              error:
                type: string
              detail:
                type: string
          409:
            description: O usuário já está cadastrado.
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
        return ResponseProductSchema.dump(update_product(args))


    @use_args(argmap={"id": fields.Int(required=True)}, location="query")
    def delete(self, args):
        """
        parameters:
          - name: target_product_id
            description: ID do produto alvo.
            in: path
            type: int
            required: true

        responses:
          201:
            description: O produto requisitado foi excluído com sucesso.
          404:
            description: O produto requisitado não foi encontrado.
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
        delete_product(args)
        return 204


api.add_resource(ProductRoutes, "/products")
