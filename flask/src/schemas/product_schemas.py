from src.extensions.ma import ma
from src.models.product_model import Product

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True
        include_relationships = True

    id = ma.auto_field(dump_only=True)