from flask import Flask

from src.database.connection import database

def create_app():
    app = Flask(__name__)
    database.init_app(app)

    @app.route(rule="/status", methods=["GET"])
    def status():
        return {"status": 200}

