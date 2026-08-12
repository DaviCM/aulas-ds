from src.extensions.db import db

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(120), nullable=False, unique=True)
    category = db.Column(db.String(120), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    value = db.Column(db.Numeric, nullable=False)

    logs = db.relationship("Log", back_populates="product", cascade="all, delete-orphan")

