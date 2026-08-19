from typing import Literal

from src.models.product_model import Product
from src.models.user_model import User
from src.schemas.product_schemas import *
from src.services.log_services import create_log
from src.errors.product_errors import *
from src.extensions.db import db

def get_product_by_id(id: int) -> Product:
    stmt = db.select(Product).where(Product.id == id)
    target_product = db.session.scalar(stmt)

    if target_product == None:
        raise ProductNotFoundError
    else:
        return target_product


def verify_product_description(target_description: str) -> Literal[True]:
    stmt = db.select(Product).where(Product.description == target_description)
    target_product = db.session.scalar(stmt)

    if target_product != None:
        raise ProductAlreadyExistsError
    else:
        return True


def create_product(data: CreateProductSchema) -> Product:
    # ! Lembrar de levantar o erro na rota
    # * Não levantei, usei o error handler
    verify_product_description(data.fields["description"])

    new_product = Product(
        description=data.fields["description"],
        category=data.fields["category"],
        quantity=data.fields["quantity"],
        value=data.fields["value"],
    )

    db.session.add(new_product)
    db.session.commit()

    create_log(target_product=new_product, type=True, quantity=data.fields["quantity"])

    return new_product


def list_products(params: QueryProductSchema) -> list[Product]:
    stmt = db.select(Product)

    if params.fields["description"] != None:
        stmt = stmt.where(params.fields["descrpition"].in_(Product.description))

    if params.fields["category"] != None:
        stmt = stmt.where(params.fields["category"] == Product.category)

    if params.fields["minimum_quantity"] != None:
        stmt = stmt.where(params.fields["minimum_quantity"] <= Product.quantity)

    if params.fields["maximum_quantity"] != None:
        stmt = stmt.where(params.fields["maximum_quantity"] >= Product.quantity)

    if params.fields["minimum_value"] != None:
        stmt = stmt.where(params.fields["minimum_value"] <= Product.value)

    if params.fields["maximum_value"] != None:
        stmt = stmt.where(params.fields["maximum_value"] >= Product.value)

    products = db.session.scalars(stmt).all()

    if products == []:
        raise ProductNotFoundError
    else:
        return products


def update_product(data: UpdateProductSchema) -> Product:
    to_edit = get_product_by_id(data.fields["id"])

    if data.fields["description"] != None:
        # * Tratamento de erro comum, levantará ProductAlreadyExistsError
        verify_product_description(data.fields["description"])

        to_edit.description = data.fields["descrpition"]

    if data.fields["category"] != None:
        to_edit.category = data.fields["category"]

    if data.fields["quantity"] != None:
        old_quantity = to_edit
        transaction_type = True if data.fields["quantity"] > to_edit.quantity else False

        to_edit.quantity = data.fields["quantity"]
        create_log(target_product=to_edit, type=transaction_type, quantity=(data.fields["quantity"] - old_quantity))

    if data.fields["value"] != None:
        to_edit.value = data.fields["value"]

    db.session.commit()
    db.session.flush()


    return to_edit


def delete_product(id: int):
    to_delete = get_product_by_id(id)

    db.session.merge(to_delete)
    db.session.delete(to_delete)

    db.session.commit()

