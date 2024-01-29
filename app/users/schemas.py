from enum import Enum
from pydantic import BaseModel


class Sex(str, Enum):
    male = "male"
    female = "female"


class User(BaseModel):
    id: int | None = None
    name: str
    password: str
    email: str
    is_teacher: bool = False
    sex: Sex
