from typing import Annotated
from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db_helper import db_helper
from .models import User
from .crud import get_user


async def user_by_id(
    user_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scope_session_dependency),
) -> User:
    user = await get_user(session=session, user_id=user_id)
    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"User {user_id} not found"
    )
