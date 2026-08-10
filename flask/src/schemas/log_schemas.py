from marshmallow import Schema, fields

class ResponseLogSchema(Schema):
    id = fields.Int(required=True)
    type = fields.Bool(required=True)
    quantity = fields.Int(required=True)
    logged_at = fields.DateTime(required=True)
    product_id = fields.Int(required=True)



response_log_schema = ResponseLogSchema()