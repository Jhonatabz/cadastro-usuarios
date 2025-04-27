from pydantic import BaseModel, EmailStr

class User(BaseModel):
    nome: str
    email: EmailStr
    senha: str

class UserPublic(BaseModel):
    id: int
    nome: str
    email: EmailStr

class UserDB(User):
    id: int

class UserList(BaseModel):
    users: list[UserPublic]