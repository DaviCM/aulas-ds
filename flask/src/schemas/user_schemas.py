from src.extensions.ma import ma
from src.models.user_model import User

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

    id = ma.auto_field(dump_only=True)
    password = ma.auto_field(load_only=True)