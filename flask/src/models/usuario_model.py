from sqlalchemy import Column, Integer, String

from src.database.base import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nome = Column(String(120), nullable=False, unique=True)
    email = Column(String(120), nullable=False, unique=True)
    senha = Column(String(255), nullable=False)
