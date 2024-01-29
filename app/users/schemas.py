from enum import Enum
from pydantic import BaseModel


class Sex(str, Enum):
    male = "male"
    female = "female"


class UserBase(BaseModel):
    name: str
    email: str
    is_teacher: bool = False
    sex: Sex

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str
    re_password: str


class User(UserBase):
    id: int | None = None
    is_active: bool = False
