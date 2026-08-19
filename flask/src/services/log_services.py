from src.models.log_model import Log
from src.models.product_model import Product
from src.schemas.log_schemas import QueryLogSchema
from src.errors.log_errors import LogNotFoundError
from src.errors.product_errors import ProductNotFoundError
from src.extensions.db import db

def create_log(target_product: Product, type: bool, quantity: int) -> Log:
    
    if target_product == None:
        raise ProductNotFoundError

    new_log = Log(
        type=type,
        quantity=quantity,
        product=target_product,
    )

    db.session.add(new_log)
    db.session.commit()

    return new_log


def list_logs(params: QueryLogSchema) -> list[Log]:

    stmt = db.select(Log)

    if params.fields["type"] != None:
            stmt = stmt.where(Log.type == params.fields["type"])

    if params.fields["minimum_quantity"] != None:
        stmt = stmt.where(Log.quantity >= params.fields["minimum_quantity"])

    if params.fields["maximum_quantity"] != None:
        stmt = stmt.where(Log.quantity <= params.fields["maximum_quantity"])

    if params.fields["minimum_date"] != None:
        stmt = stmt.where(Log.logged_at >= params.fields["minimum_date"])

    if params.fields["maximum_date"] != None:
        stmt = stmt.where(Log.logged_at <= params.fields["maximum_date"])

    if params.fields["product_id"] != None:
        stmt = stmt.where(Log.product_id == params.fields["product_id"])

    logs = db.session.scalars(stmt).all()

    if logs == []:
        raise LogNotFoundError
    else:
        return logs

