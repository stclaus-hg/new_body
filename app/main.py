from fastapi import FastAPI
from app.users.schemas import Sex


app = FastAPI()


@app.get("/")
async def root():
    return {"msg": "Hello World"}


@app.get("/user/{user_id}")
async def user(user_id: int):
    return {"name": "John" if user_id == 1 else "Unknown", "user_id": user_id}


@app.get("/users/{sex}")
async def users_by_sex(sex: Sex):
    if sex == Sex.male:
        return "john"
    else:
        return "joan"
