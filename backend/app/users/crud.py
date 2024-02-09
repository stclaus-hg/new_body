from sqlalchemy.ext.asyncio import AsyncSession
from app.users.models import User
from app.users.schemas import UserCreate
from sqlalchemy import select
from sqlalchemy.engine import Result


async def get_users(session: AsyncSession) -> list[User]:
    stmt = select(User).order_by(User.name)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()
    return list(users)

async def create_user(session: AsyncSession, user_in: UserCreate) -> User:
    hashed_password = user_in.password + "fakehashed"
    db_user = User(
        name=user_in.name,
        email=user_in.email,
        sex=user_in.sex,
        hashed_password=hashed_password,
        is_coach=user_in.is_coach,
    )
    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)
    return db_user

