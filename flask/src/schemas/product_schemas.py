from marshmallow import Schema, fields, validate as v

class CreateProductSchema(Schema):
    description = fields.Str(validate=v.Length(max=120), required=True)
    category = fields.Str(validate=v.Length(max=120), required=True)
    quantity = fields.Int(required=True)
    value = fields.Decimal(required=True)



class UpdateProductSchema(Schema):
    id = fields.Int(required=True, allow_none=False)
    description = fields.Str(validate=v.Length(max=120), required=False, allow_none=True)
    category = fields.Str(validate=v.Length(max=120), required=False, allow_none=True)
    quantity = fields.Int(required=False, allow_none=True)
    value = fields.Decimal(required=False, allow_none=True)



class QueryProductSchema(Schema):
    description = fields.Str(validate=v.Length(max=120), required=False, allow_none=True)
    category = fields.Str(validate=v.Length(max=120), required=False, allow_none=True)
    minimum_quantity = fields.Int(required=False, allow_none=True)
    maximum_quantity = fields.Int(required=False, allow_none=True)
    minimum_value = fields.Decimal(required=False, allow_none=True)
    maximum_value = fields.Decimal(required=False, allow_none=True)



class ResponseProductSchema(Schema):
    id = fields.Int(required=True, allow_none=False)
    description = fields.Str(validate=v.Length(max=120), required=True)
    category = fields.Str(validate=v.Length(max=120), required=True)
    quantity = fields.Int(required=True)
    value = fields.Decimal(required=True)

