from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

argon2 = PasswordHasher()

def hash_password(target_password: str) -> str:
    return argon2.hash(target_password)


def verify_password(hashed_password: str, target_password: str) -> bool:
    try:
        # Sempre retorna True, caso contrário levanta uma exeção
        return argon2.verify(hashed_password, target_password)
    
    except VerifyMismatchError:
        # Essa é a exceção levantada para senhas que não batem com o hash
        return False

