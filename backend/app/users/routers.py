from fastapi import APIRouter, Depends
from .schemas import UserCreate
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db_helper import db_helper
from app.users import crud

router = APIRouter(tags=["users"])


@router.get("/")
async def get_users(session: AsyncSession=Depends(db_helper.scope_session_dependency)):
    return await crud.get_users(session=session)


@router.post("/")
async def user_sign_up(user: UserCreate, session: AsyncSession=Depends(db_helper.scope_session_dependency)):
    return await crud.create_user(session=session, user_in=user)

