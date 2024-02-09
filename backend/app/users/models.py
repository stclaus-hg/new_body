from app.core.models import Base
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]
    is_coach: Mapped[bool] = mapped_column(default=False)
    sex: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=False)
