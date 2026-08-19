from src.errors.app_errors import AppError

class LogNotFoundError(AppError):
    code = 404
    name = "LOG_NOT_FOUND_ERROR"
    detail = "O log requisitado não foi encontrado. Por favor, tente novamente."