from os import getenv

from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

database = SQLAlchemy(engine_options=
                      {"url": getenv("DATABASE_URL"),
                       "echo": True,
                       "pool_pre_ping": True,
                       "pool_size": 20,
                       "max_overflow": 0}
                       )

