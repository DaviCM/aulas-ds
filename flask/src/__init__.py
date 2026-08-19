from os import getenv

from flask import Flask
from dotenv import load_dotenv

from src.extensions.api import api
from src.extensions.db import db
from src.extensions.ma import ma
from src.extensions.swagger import swagger

from src.schemas.user_schemas import *
from src.schemas.product_schemas import *
from src.schemas.log_schemas import *
from src.errors.app_errors import AppError

load_dotenv()

class Config():
    SQLALCHEMY_DATABASE_URI = getenv("DATABASE_URL")  
    SQLALCHEMY_ENGINE_OPTIONS = {"url": getenv("DATABASE_URL"),
                                "echo": True,
                                "pool_pre_ping": True,
                                "pool_size": 20,
                                "max_overflow": 0}

    SWAGGER = {
        "specs_route": "/docs",
        "template": {
            "definitions": {
                "CreateUser": CreateUserSchema,
                "LoginUser": LoginUserSchema,
                "UpdateUser": UpdateUserSchema,
                "ResponseUser": ResponseUserSchema,

                "CreateProduct": CreateProductSchema,
                "UpdateProduct": UpdateProductSchema,
                "QueryProduct": QueryProductSchema,
                "ResponseProduct": ResponseProductSchema,

                "QueryLog": QueryLogSchema,
                "ResponseLog": ResponseLogSchema
            },
        }
    }


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)
    api.init_app(app)
    swagger.init_app(app)

    @app.errorhandler(AppError)
    def handle_app_error(error: AppError):
        return {
            "status_code": error.code,
            "error": error.name,
            "detail": error.detail
        }, error.code

    return app
