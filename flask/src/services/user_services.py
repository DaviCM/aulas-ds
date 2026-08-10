from marshmallow import ValidationError

from src.models.user_model import User
from src.schemas.user_schemas import create_user_schema, response_user_schema
from src.services.email_services import *
from src.services.password_services import *
from src.errors.user_errors import *
from src.extensions.db import db


def get_user_by_id(id: int) -> User:
    stmt = db.select(User).where(User.id == id)
    target_user = db.session.scalar(stmt)

    if target_user == None:
        raise UserNotFoundError
    else:
        return target_user



def create_user(data: dict):
    if email_already_exists(data["email"] == True):
        raise InvalidUserError

    if verify_email(data["email"] == False):
        raise InvalidUserError

    new_user = User(
        name=data["name"],
        email=data["email"],
        password=hash_password(data["password"]),
    )

    db.session.add(new_user)
    db.session.commit()

    return response_user_schema.dump(new_user)



def login(target_email: str, target_password: str) -> User:
    if email_already_exists(target_email) == False:
        raise UserNotFoundError

    stmt = db.select(User).where(User.email == target_email)
    logged_user = db.session.scalar(stmt)

    if verify_password(logged_user.password, target_password) == False:
        raise InvalidCredentialsError

    return logged_user



def update_user(id: int, data: dict):
    to_edit = get_user_by_id(id)
    
    if (data["email"] != None) and (email_already_exists(data["email"]) == True):
        raise InvalidUserError

    if (data["email"] != None) and (verify_email(data["email"]) == False):
        raise InvalidUserError

    if data["name"] != None:
       to_edit.name = data["name"]

    if data["email"] != None:
        to_edit.name = data["email"]

    if data["password"] != None:
        to_edit.name = hash_password(data["password"])

    db.session.commit()
    db.session.flush()

    return response_user_schema.dump(to_edit)



def delete_user(id: int):
    to_delete = get_user_by_id(id)

    db.session.merge(to_delete)
    db.session.delete(to_delete)

    db.session.commit()


