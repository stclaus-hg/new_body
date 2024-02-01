from fastapi import FastAPI
from app.users import models
from app.users.routers import router as user_router
from app.core.database import engine, SessionLocal


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user_router)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"msg": "Hello World"}
