from email_validator import validate_email, EmailNotValidError

from src.models.user_model import User
from src.extensions.db import db

def email_already_exists(email: str) -> bool:
    stmt = db.select(User.email).where(User.email == email)
    result = db.session.scalar(stmt)

    return False if result == None else True


def verify_email(email: str) -> bool:
    try:
        validate_email(email)
        return True
    
    except EmailNotValidError:
        return False

