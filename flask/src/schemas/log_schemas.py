from src.extensions.ma import ma
from src.models.log_model import Log

class LogSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Log
        load_instance = True
        include_relationships = True
        include_fk = True

    id = ma.auto_field(dump_only=True)
    product_id = ma.auto_field(dump_only=True)