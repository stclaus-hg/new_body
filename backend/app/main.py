from fastapi import FastAPI
from app.users import models
from app.users.routers import router as user_router
from app.core.db_helper import engine, SessionLocal, db_helper
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)     
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(user_router, prefix="/users")


@app.get("/")
async def root():
    return {"msg": "Hello World"}
