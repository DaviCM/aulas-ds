from src.models.user_model import User
from src.schemas.user_schemas import CreateUserSchema, UpdateUserSchema
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


def create_user(data: CreateUserSchema) -> User:
    if email_already_exists(data.fields["email"] == True):
        raise UserAlreadyExistsError

    if verify_email(data.fields["email"] == False):
        raise InvalidUserError

    new_user = User(
        name=data.fields["name"],
        email=data.fields["email"],
        password=hash_password(data.fields["password"]),
    )

    db.session.add(new_user)
    db.session.commit()

    return new_user


def login(target_email: str, target_password: str) -> User:
    if email_already_exists(target_email) == False:
        raise UserNotFoundError

    stmt = db.select(User).where(User.email == target_email)
    logged_user = db.session.scalar(stmt)

    if verify_password(logged_user.password, target_password) == False:
        raise InvalidCredentialsError

    return logged_user


def update_user(data: UpdateUserSchema) -> User:
    to_edit = get_user_by_id(data.fields["id"])
    
    if (data.fields["email"] != None) and (email_already_exists(data.fields["email"]) == True):
        raise InvalidUserError

    if (data.fields["email"] != None) and (verify_email(data.fields["email"]) == False):
        raise InvalidUserError

    if data.fields["name"] != None:
       to_edit.name = data.fields["name"]

    if data.fields["email"] != None:
        to_edit.email = data.fields["email"]

    if data.fields["password"] != None:
        to_edit.password = hash_password(data.fields["password"])

    db.session.commit()
    db.session.flush()

    return to_edit


def delete_user(id: int):
    to_delete = get_user_by_id(id)

    db.session.merge(to_delete)
    db.session.delete(to_delete)

    db.session.commit()


