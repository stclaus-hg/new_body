from fastapi import APIRouter
from .schemas import UserCreate


router = APIRouter()


@router.post("/users/", tags=["users"])
async def user_sign_up(user: UserCreate):
    return user.model_dump()
