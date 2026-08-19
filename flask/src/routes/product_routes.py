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
        """
        return ResponseProductSchema.dump(create_product(args))


    @use_args(argmap=QueryProductSchema, location="json")
    def get(self, args):
        """
        """
        return ResponseProductSchema.dump(list_products(args), many=True)


    @use_args(argmap=UpdateProductSchema, location="json")
    def patch(self, args):
        """
        """
        return ResponseProductSchema.dump(update_product(args))


    @use_args(argmap={"id": fields.Int(required=True)}, location="query")
    def delete(self, args):
        """
        """
        delete_product(args)
        return 204


api.add_resource(ProductRoutes, "/products")
