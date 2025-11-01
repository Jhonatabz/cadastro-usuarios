from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(BaseModel):
    nome: str
    email: EmailStr
    senha: str

    def to_db(self) -> dict:
        """Prepare a dict suitable for DB insertion (hash password)."""
        return {"nome": self.nome, "email": self.email, "senha": pwd_context.hash(self.senha)}


class UserVerify(BaseModel):
    email: EmailStr
    senha: str


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)