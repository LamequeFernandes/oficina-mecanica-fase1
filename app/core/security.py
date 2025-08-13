from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from app.core.config import settings  # SECRET_KEY, ALGORITHM

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def criar_hash_senha(senha: str) -> str:
    """Gera o hash bcrypt da senha."""
    return pwd_context.hash(senha)

def verificar_senha(senha: str, hash_senha: str) -> bool:
    """Compara a senha com seu hash."""
    return pwd_context.verify(senha, hash_senha)

def criar_token_jwt(usuario_id: int) -> str:
    """Gera um token JWT válido por 24 horas."""
    expira = datetime.utcnow() + timedelta(hours=24) # type: ignore
    payload = {"sub": str(usuario_id), "exp": expira} # type: ignore
    return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM) # type: ignore

def decodificar_token_jwt(token: str) -> int | None:
    """Valida o token e retorna o ID do usuário."""
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return int(payload.get("sub")) # type: ignore
    except (JWTError, ValueError):
        return None
