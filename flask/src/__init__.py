from os import getenv

from flask import Flask
from dotenv import load_dotenv

from src.extensions.db import db
from src.extensions.ma import ma

load_dotenv()

class Config():
    SQLALCHEMY_DATABASE_URI = getenv("DATABASE_URL")  


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)

    return app
