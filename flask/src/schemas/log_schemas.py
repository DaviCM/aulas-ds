from marshmallow import Schema, fields

class QueryLogSchema(Schema):
    type = fields.Bool(required=False, allow_none=True)
    minimum_quantity = fields.Int(required=False, allow_none=True)
    maximum_quantity = fields.Int(required=False, allow_none=True)
    minimum_date = fields.DateTime(required=False, allow_none=True)
    maximum_date = fields.DateTime(required=False, allow_none=True)
    product_id = fields.Int(required=False, allow_none=True)



class ResponseLogSchema(Schema):
    id = fields.Int(required=True)
    type = fields.Bool(required=True)
    quantity = fields.Int(required=True)
    logged_at = fields.DateTime(required=True)
    product_id = fields.Int(required=True)
