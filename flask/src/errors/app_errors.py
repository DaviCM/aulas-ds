class AppError(Exception):
    code = 500
    name = "APP_ERROR"
    detail = "Ocorreu um erro inesperado na aplicação, verifique a integridade do banco."