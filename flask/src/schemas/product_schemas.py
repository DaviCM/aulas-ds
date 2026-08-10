from marshmallow import Schema, fields, validate as v

class CreateProductSchema(Schema):
    description = fields.Str(validate=v.Length(max=120), required=True)
    category = fields.Str(validate=v.Length(max=120), required=True)
    quantity = fields.Int(required=True)
    value = fields.Decimal(required=True)



class UpdateProductSchema(Schema):
    description = fields.Str(validate=v.Length(max=120), required=True, allow_none=True)
    category = fields.Str(validate=v.Length(max=120), required=True, allow_none=True)
    quantity = fields.Int(required=True, allow_none=True)
    value = fields.Decimal(required=True, allow_none=True)



class ResponseProductSchema(Schema):
    id = fields.Int(required=True)
    description = fields.Str(validate=v.Length(max=120), required=True)
    category = fields.Str(validate=v.Length(max=120), required=True)
    quantity = fields.Int(required=True)
    value = fields.Decimal(required=True)



create_product_schema = CreateProductSchema()
update_product_schema = UpdateProductSchema()
response_product_schema = ResponseProductSchema()