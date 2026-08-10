from src.errors.app_errors import AppError

class InvalidUserError(AppError):
    code = 400
    name = "INVALID_USER_ERROR"
    detail = "As informações de usuário fornecidas são inválidas. Por favor, tente novamente."



class InvalidCredentialsError(AppError):
    code = 401
    name = "INVALID_CREDENTIALS_ERROR"
    detail = "As credenciais fornecidas são inválidas. Por favor, tente novamente."



class UserNotFoundError(AppError):
    code = 404
    name = "USER_NOT_FOUND_ERROR"
    detail = "O usuário requisitado não foi encontrado. Por favor, tente novamente."



class UserAlreadyExistsError(AppError):
    code = 409
    name = "USER_ALREADY_EXISTS_ERROR"
    detail = "O usuário já está cadastrado. Por favor, tente realizar login ou cadastrar outro usuário."


