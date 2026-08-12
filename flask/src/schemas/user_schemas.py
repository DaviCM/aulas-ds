from marshmallow import Schema, fields, validate as v

class CreateUserSchema(Schema):
    name = fields.Str(validate=v.Length(max=120), required=True)
    email = fields.Str(validate=v.Length(max=120), required=True)
    password = fields.Str(validate=v.Length(max=255), required=True)



class LoginUserSchema(Schema):
    email = fields.Str(validate=v.Length(max=120), required=True)
    password = fields.Str(validate=v.Length(max=255), required=True)



class UpdateUserSchema(Schema):
    id = fields.Int(required=True, allow_none=False)
    name = fields.Str(validate=v.Length(max=120), required=True, allow_none=True)
    email = fields.Str(validate=v.Length(max=120), required=True, allow_none=True)
    password = fields.Str(validate=v.Length(max=255), required=True, allow_none=True)



class ResponseUserSchema(Schema):
    id = fields.Int(required=False, allow_none=True)
    name = fields.Str(validate=v.Length(max=120), required=True)
    email = fields.Str(validate=v.Length(max=120), required=True)