from src.database.connection import db

class Log(db.Model):
    __tablename__ = "logs"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Boolean, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    logged_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    product_id = db.Column(db.ForeignKey("products.id", ondelete="cascade"), nullable=False)

    product = db.relationship("Product", back_populates="logs")
