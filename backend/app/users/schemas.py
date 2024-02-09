from enum import Enum
from pydantic import BaseModel, ConfigDict


class Sex(str, Enum):
    male = "male"
    female = "female"


class UserBase(BaseModel):
    name: str
    email: str
    is_coach: bool = False
    sex: Sex

    class ConfigDict:
        from_attributes = True


class UserCreate(UserBase):
    password: str
    re_password: str


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int | None = None
    is_active: bool = False
