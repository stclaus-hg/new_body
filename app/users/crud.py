from sqlalchemy.orm import Session
from app.users import models, schemas


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = user.password + "fakehashed"
    db_user = models.User(
        name=user.name,
        email=user.email,
        sex=user.sex,
        hashed_password=hashed_password,
        is_coach=user.is_coach,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
