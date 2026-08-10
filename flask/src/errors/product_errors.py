from src.errors.app_errors import AppError

class InvalidProductError(AppError):
    code = 400
    name = "INVALID_PRODUCT_ERROR"
    detail = "As informações de produto fornecidas são inválidas. Por favor, tente novamente."



class ProductNotFoundError(AppError):
    code = 404
    name = "PRODUCT_NOT_FOUND_ERROR"
    detail = "O produto requisitado não foi encontrado. Por favor, tente novamente."



class ProductAlreadyExistsError(AppError):
    code = 409
    name = "PRODUCT_ALREADY_EXISTS_ERROR"
    detail = "O produto já está cadastrado. Por favor, tente cadastrar outro produto."