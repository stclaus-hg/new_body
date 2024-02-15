from fastapi import APIRouter, Depends, status
from .schemas import UserCreate, User, UserUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db_helper import db_helper
from . import crud
from .dependencies import user_by_id
from .models import User as UserModel

router = APIRouter(tags=["users"])


@router.get("/", response_model=list[User])
async def get_users(
    session: AsyncSession = Depends(db_helper.scope_session_dependency),
):
    return await crud.get_users(session=session)


@router.get("/{user_id}/", response_model=User)
async def get_user(user: User = Depends(user_by_id)):
    return user


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(
    user: UserCreate,
    session: AsyncSession = Depends(db_helper.scope_session_dependency),
):
    return await crud.create_user(session=session, user_in=user)


@router.patch("/{user_id}/", response_model=User)
async def update_user(
    user_in: UserUpdate,
    user: UserModel = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.scope_session_dependency),
):
    return await crud.update_user(session=session, user=user, user_in=user_in)


@router.delete("/{user_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user: UserModel = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.scope_session_dependency),
):
    await crud.delete_user(session=session, user=user)