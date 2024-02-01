from app.core.database import Base
from sqlalchemy import Column, Integer, String, Boolean


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    is_coach = Column(Boolean, default=False)
    sex = Column(String)
    is_active = Column(Boolean, default=False)
