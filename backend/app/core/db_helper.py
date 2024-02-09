from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession, async_scoped_session
from app.core.config import settings
from asyncio import current_task
from typing import AsyncGenerator

SQLALCHEMY_DATABASE_URL = "sqlite:///.sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class DatabaseHelper:
    def __init__(self, url: str, echo: bool) -> None:
        self.engine = create_async_engine(url=url, echo=echo)
        self.session_factory = async_sessionmaker(
            bind=self.engine, autoflush=False, autocommit=False, expire_on_commit=False
        )

    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task
        )
        return session

    async def scope_session_dependency(self) -> AsyncGenerator[AsyncSession, None]:
        session = self.get_scoped_session()
        yield session
        await session.close()


db_helper = DatabaseHelper(settings.db_url, settings.db_echo)
