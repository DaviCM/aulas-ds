from marshmallow import Schema, fields, validate as v

class CreateUserSchema(Schema):
    name = fields.Str(validate=v.Length(max=120), required=True)
    email = fields.Str(validate=v.Length(max=120), required=True)
    password = fields.Str(validate=v.Length(max=255), required=True)



class UpdateUserSchema(Schema):
    name = fields.Str(validate=v.Length(max=120), required=True, allow_none=True)
    email = fields.Str(validate=v.Length(max=120), required=True, allow_none=True)
    password = fields.Str(validate=v.Length(max=255), required=True, allow_none=True)



class ResponseUserSchema(Schema):
    id = fields.Int(allow_none=True, required=False)
    name = fields.Str(validate=v.Length(max=120), required=True)
    email = fields.Str(validate=v.Length(max=120), required=True)



create_user_schema = CreateUserSchema()
update_user_schema = UpdateUserSchema()
response_user_schema = ResponseUserSchema()
